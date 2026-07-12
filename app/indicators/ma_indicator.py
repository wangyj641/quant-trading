import pandas as pd

from app.indicators.base_indicator import Indicator


class MAIndicator(Indicator):

    def __init__(
        self,
        period: int,
    ):
        self.period = period

    def calculate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        df[f"MA{self.period}"] = df["close"].rolling(self.period).mean()

        return df
