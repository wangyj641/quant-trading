import pandas as pd

from app.indicators.base_indicator import Indicator


class MAIndicator(Indicator):

    def __init__(
        self,
        period: int,
    ):
        self.period = period

    def calculate(self, df):

        return df["close"].rolling(self.period).mean()

    @property
    def column_name(self):

        return f"MA{self.period}"
