import pandas as pd

from app.domain.signal import Signal
from app.strategy.base_strategy import Strategy


class MACrossStrategy(Strategy):

    def run(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        result = df.copy()

        result["signal"] = Signal.HOLD.value

        buy = (result["MA5"] > result["MA20"]) & (
            result["MA5"].shift(1) <= result["MA20"].shift(1)
        )

        sell = (result["MA5"] < result["MA20"]) & (
            result["MA5"].shift(1) >= result["MA20"].shift(1)
        )

        result.loc[buy, "signal"] = Signal.BUY.value

        result.loc[sell, "signal"] = Signal.SELL.value

        return result
