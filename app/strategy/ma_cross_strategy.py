import pandas as pd

from app.domain.signal import SignalType
from app.strategy.base_strategy import Strategy

from app.domain.trading_signal import TradingSignal
from app.domain.trading_signal import SignalType


class MACrossStrategy(Strategy):

    def generate(
        self,
        symbol: str,
        df: pd.DataFrame,
    ) -> list[TradingSignal]:

        signals = []

        for i in range(1, len(df)):

            prev = df.iloc[i - 1]
            curr = df.iloc[i]

            if prev["MA5"] <= prev["MA20"] and curr["MA5"] > curr["MA20"]:
                signals.append(
                    TradingSignal(
                        symbol=symbol,
                        datetime=df.index[i],
                        signal=SignalType.BUY,
                    )
                )

            elif prev["MA5"] >= prev["MA20"] and curr["MA5"] < curr["MA20"]:
                signals.append(
                    TradingSignal(
                        symbol=symbol,
                        datetime=df.index[i],
                        signal=SignalType.SELL,
                    )
                )

        return signals
