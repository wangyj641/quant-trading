from dataclasses import dataclass

import pandas as pd


@dataclass(slots=True)
class BenchmarkResult:

    initial_cash: float
    final_equity: float
    total_return: float
    equity_curve: pd.Series


class BuyAndHoldBenchmark:

    def run(
        self,
        df: pd.DataFrame,
        initial_cash: float = 100_000,
    ) -> BenchmarkResult:

        if df.empty:
            raise ValueError("Cannot run benchmark with empty data")

        initial_price = float(df["close"].iloc[0])

        shares = initial_cash / initial_price

        equity = df["close"] * shares

        final_equity = float(equity.iloc[-1])

        total_return = (final_equity / initial_cash) - 1

        return BenchmarkResult(
            initial_cash=initial_cash,
            final_equity=final_equity,
            total_return=total_return,
            equity_curve=equity,
        )
