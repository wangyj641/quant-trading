import pandas as pd
from app.backtest.report import BacktestReport


class BacktestEngine:

    def run(
        self,
        df: pd.DataFrame,
    ) -> BacktestReport:
        pass
