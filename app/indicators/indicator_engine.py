import pandas as pd

from app.indicators.base_indicator import Indicator


class IndicatorEngine:

    def __init__(self):

        self.indicators = []

    def register(
        self,
        indicator: Indicator,
    ):

        self.indicators.append(indicator)

    def calculate(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        for indicator in self.indicators:

            df = indicator.calculate(df)

        return df
