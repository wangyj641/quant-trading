from app.backtest.report import BacktestReport

import pandas as pd


class BacktestEngine:

    def __init__(
        self,
        execution_engine,
    ):
        self.execution_engine = execution_engine

    def calculate_equity(
        self,
        df,
        execution_result,
    ):

        equity = []

        for index, row in df.iterrows():

            price = float(row["close"])

            total_value = execution_result.portfolio.cash

            for position in execution_result.portfolio.positions.values():

                total_value += position.quantity * price

            equity.append(
                {
                    "datetime": index,
                    "value": total_value,
                }
            )

        return pd.DataFrame(equity).set_index("datetime")["value"]

    def run(
        self,
        df,
        signals,
    ) -> BacktestReport:

        execution_result = self.execution_engine.execute(
            df=df,
            signals=signals,
        )

        equity_curve = self.calculate_equity(
            df,
            execution_result,
        )

        total_return = (
            equity_curve.iloc[-1] - self.execution_engine.initial_cash
        ) / self.execution_engine.initial_cash

        win_rate = (
            sum(1 for trade in execution_result.portfolio.trades if trade.profit > 0)
            / len(execution_result.portfolio.trades)
            if execution_result.portfolio.trades
            else 0
        )

        max_drawdown = (equity_curve.cummax() - equity_curve).max()
        trades = execution_result.portfolio.trades

        return BacktestReport(
            initial_cash=self.execution_engine.initial_cash,
            final_cash=execution_result.portfolio.cash,
            total_return=total_return,
            trade_count=len(execution_result.portfolio.trades),
            win_rate=win_rate,
            max_drawdown=max_drawdown,
            trades=trades,
            equity_curve=equity_curve,
        )
