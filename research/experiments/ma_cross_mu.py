from app.database.repository import PriceRepository
from app.strategy.ma_cross_strategy import MACrossStrategy
from app.domain.timeframe import TimeFrame

from research.runner import ResearchRunner
from research.benchmark import BuyAndHoldBenchmark

from app.constants.common import INITIAL_CASH, SYMBOL

from research.plot import (
    plot_price,
    plot_equity_curve,
)

import pandas as pd


def main():

    repository = PriceRepository()

    runner = ResearchRunner(
        repository=repository,
    )

    df = runner.load_data(
        symbol=SYMBOL,
        timeframe=TimeFrame.DAY_1,
    )

    strategy = MACrossStrategy(
        short_window=20,
        long_window=50,
    )

    report = runner.run(
        symbol=SYMBOL,
        strategy=strategy,
        timeframe=TimeFrame.DAY_1,
        initial_cash=INITIAL_CASH,
    )

    benchmark = BuyAndHoldBenchmark()

    benchmark_result = benchmark.run(
        df=df,
        initial_cash=INITIAL_CASH,
    )

    print()
    print("=" * 60)
    print("Backtest Report")
    print("=" * 60)

    print(f"Symbol          : {SYMBOL}")
    print(f"Initial Cash    : " f"${report.initial_cash:,.2f}")

    print(f"Final Cash      : " f"${report.final_cash:,.2f}")

    print(f"Final Equity    : " f"${report.final_equity:,.2f}")

    print(f"Total Return    : " f"{report.total_return:.2%}")

    print(f"Max Drawdown    : " f"{report.max_drawdown:.2%}")

    print(f"Volatility      : " f"{report.volatility:.2%}")

    print(f"Sharpe Ratio    : " f"{report.sharpe_ratio:.2f}")

    print(f"Win Rate        : " f"{report.win_rate:.2%}")

    print(f"Gross Profit    : " f"${report.gross_profit:,.2f}")

    print(f"Gross Loss      : " f"${report.gross_loss:,.2f}")

    print(f"Profit Factor   : " f"{report.profit_factor:.2f}")

    print(f"Closed Trades   : " f"{len(report.trades)}")

    print(f"Open Trades     : " f"{len(report.open_trades)}")

    print(f"Trades          : " f"{len(report.trades)}")

    for i, trade in enumerate(report.trades, start=1):
        print(f"Trade {i}: {trade}")

    print("=" * 60)

    print()

    print("=" * 70)
    print("Strategy vs Buy & Hold")
    print("=" * 70)

    print(f"Strategy Return : " f"{report.total_return:.2%}")

    print(f"Buy & Hold      : " f"{benchmark_result.total_return:.2%}")

    print(
        f"Difference      : "
        f"{report.total_return - benchmark_result.total_return:.2%}"
    )

    print("=" * 70)

    print(f"Data rows           : {len(df)}")

    print(f"Equity curve points : " f"{len(report.equity_curve.points)}")

    print(report.equity_curve.points[0])

    print(report.equity_curve.points[-1])

    print("=" * 70)

    plot_price(
        df=df,
        short_window=20,
        long_window=50,
        trades=report.trades,
    )

    plot_equity_curve(
        report=report,
        benchmark_result=benchmark_result,
    )


if __name__ == "__main__":
    main()
