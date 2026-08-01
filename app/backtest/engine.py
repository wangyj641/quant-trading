from __future__ import annotations

import pandas as pd

from app.backtest.equity_curve import EquityCurve
from app.backtest.metrics import BacktestMetrics
from app.backtest.report import BacktestReport
from app.execution.backtest_execution import BacktestExecution
from app.strategy.base_strategy import Strategy


class BacktestEngine:

    def __init__(
        self,
        strategy: Strategy,
        initial_cash: float = 100_000,
    ):
        self.strategy = strategy
        self.initial_cash = initial_cash

    def run(
        self,
        df: pd.DataFrame,
        symbol: str,
    ) -> BacktestReport:

        # Generate trading signals
        signals = self.strategy.generate_signals(
            df=df,
            symbol=symbol,
        )

        # Execute signals
        execution = BacktestExecution(initial_cash=self.initial_cash)

        result = execution.execute(
            df=df,
            signals=signals,
            symbol=symbol,
        )

        portfolio = result.portfolio

        # Build equity curve
        equity_curve = self._build_equity_curve(portfolio)

        # Calculate metrics
        total_return = BacktestMetrics.total_return(
            initial_value=self.initial_cash,
            final_value=equity_curve.final_value,
        )

        max_drawdown = BacktestMetrics.max_drawdown(equity_curve.values)

        volatility = BacktestMetrics.volatility(equity_curve.values)

        sharpe_ratio = BacktestMetrics.sharpe_ratio(equity_curve.values)

        cagr = BacktestMetrics.cagr(
            initial_value=self.initial_cash,
            final_value=equity_curve.final_value,
            years=len(equity_curve.values),
        )

        return BacktestReport(
            initial_cash=self.initial_cash,
            final_cash=portfolio.cash,
            final_equity=equity_curve.final_value,
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
