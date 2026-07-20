# import pandas as pd


class IndicatorEngine:

    def __init__(self):

        self.indicators = []

    def register(self, indicator):

        self.indicators.append(indicator)

    def calculate(self, df):

        result = df.copy()

        for indicator in self.indicators:

            result[indicator.column_name] = indicator.calculate(result)

        return result
