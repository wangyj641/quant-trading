from __future__ import annotations

import pandas as pd

from app.backtest.report import BacktestReport
from app.execution.backtest_execution import BacktestExecution
from app.backtest.equity_curve import EquityCurve
from app.backtest.metrics import BacktestMetrics


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

        equity_curve = self._build_equity_curve(portfolio)

        final_equity = equity_curve.final_value

        total_return = BacktestMetrics.total_return(
            initial_value=self.initial_cash,
            final_value=final_equity,
        )

        max_drawdown = BacktestMetrics.max_drawdown(
            equity_values=equity_curve.values,
        )

        volatility = BacktestMetrics.volatility(
            equity_values=equity_curve.values,
        )

        sharpe_ratio = BacktestMetrics.sharpe_ratio(
            equity_values=equity_curve.values,
        )

        cagr = BacktestMetrics.cagr(
            initial_value=self.initial_cash,
            final_value=final_equity,
            years=1,  # Replace with actual number of years
        )

        return BacktestReport(
            initial_cash=self.initial_cash,
            final_cash=portfolio.cash,
            final_equity=final_equity,
            total_return=total_return,
            max_drawdown=max_drawdown,
            volatility=volatility,
            sharpe_ratio=sharpe_ratio,
            cagr=cagr,
            trades=portfolio.trades,
            equity_curve=equity_curve,
        )

    def _build_equity_curve(
        self,
        portfolio,
    ) -> EquityCurve:

        curve = EquityCurve()

        for snapshot in portfolio.snapshots:

            curve.add(
                datetime=snapshot.datetime,
                equity=snapshot.total_value,
            )

        return curve
