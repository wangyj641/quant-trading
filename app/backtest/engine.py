from __future__ import annotations

import pandas as pd

from app.backtest.report import BacktestReport
from app.execution.backtest_execution import BacktestExecution


class BacktestEngine:

    def __init__(
        self,
        initial_cash: float = 10000,
    ):
        self.initial_cash = initial_cash

    def run(
        self,
        df: pd.DataFrame,
        signals,
        symbol: str,
    ) -> BacktestReport:

        execution = BacktestExecution(initial_cash=self.initial_cash)

        result = execution.execute(
            df=df,
            signals=signals,
            symbol=symbol,
        )

        portfolio = result.portfolio

        final_equity = self._get_final_equity(portfolio)

        total_return = (final_equity - self.initial_cash) / self.initial_cash

        return BacktestReport(
            initial_cash=self.initial_cash,
            final_cash=portfolio.cash,
            final_equity=final_equity,
            total_return=total_return,
            trades=portfolio.trades,
        )

    def _get_final_equity(
        self,
        portfolio,
    ) -> float:

        if not portfolio.snapshots:
            return portfolio.initial_cash

        return portfolio.snapshots[-1].total_value
