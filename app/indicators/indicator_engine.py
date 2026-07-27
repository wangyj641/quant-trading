# import pandas as pd
from app.indicators.ma_indicator import MAIndicator


class IndicatorEngine:

    def __init__(self):

        self.indicators = []

    def register(self, indicator):

        self.indicators.append(indicator)

    def add_ma(self, df, period):

        indicator = MAIndicator(period)
        self.indicators.append(indicator)

    def calculate(self, df):

        result = df.copy()

        for indicator in self.indicators:

            result[indicator.column_name] = indicator.calculate(result)

        return result
