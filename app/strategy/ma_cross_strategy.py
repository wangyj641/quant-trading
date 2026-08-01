import pandas as pd

from app.domain.trading_signal import (
    TradingSignal,
    SignalType,
)
from app.strategy.base_strategy import Strategy


class MACrossStrategy(Strategy):

    def __init__(
        self,
        short_window: int = 20,
        long_window: int = 50,
    ):
        if short_window >= long_window:
            raise ValueError("short_window must be smaller " "than long_window")

        self.short_window = short_window
        self.long_window = long_window

    def generate_signals(
        self,
        df: pd.DataFrame,
        symbol: str,
    ) -> list[TradingSignal]:

        data = df.copy()

        data["short_ma"] = data["close"].rolling(self.short_window).mean()

        data["long_ma"] = data["close"].rolling(self.long_window).mean()

        signals = []

        previous_short = None
        previous_long = None

        for index, row in data.iterrows():

            short_ma = row["short_ma"]
            long_ma = row["long_ma"]

            if pd.isna(short_ma) or pd.isna(long_ma):
                continue

            if previous_short is not None and previous_long is not None:

                # Golden Cross
                if previous_short <= previous_long and short_ma > long_ma:
                    signals.append(
                        TradingSignal(
                            symbol=symbol,
                            datetime=index,
                            signal=SignalType.BUY,
                        )
                    )

                # Death Cross
                elif previous_short >= previous_long and short_ma < long_ma:
                    signals.append(
                        TradingSignal(
                            symbol=symbol,
                            datetime=index,
                            signal=SignalType.SELL,
                        )
                    )

            previous_short = short_ma
            previous_long = long_ma

        return signals
