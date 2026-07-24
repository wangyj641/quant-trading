import pandas as pd


class Metrics:

    @staticmethod
    def max_drawdown(equity: pd.Series) -> float:
        """
        返回最大回撤，例如：
        -0.25 表示最大回撤25%
        """

        rolling_max = equity.cummax()

        drawdown = (equity - rolling_max) / rolling_max

        return drawdown.min()
