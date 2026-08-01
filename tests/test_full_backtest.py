import pandas as pd

from app.backtest.engine import BacktestEngine
from app.strategy.ma_cross_strategy import MACrossStrategy


def test_full_backtest():

    dates = pd.date_range(
        "2026-01-01",
        periods=100,
        freq="D",
    )

    prices = list(range(100, 200))

    df = pd.DataFrame(
        {
            "close": prices,
        },
        index=dates,
    )

    strategy = MACrossStrategy(
        short_window=5,
        long_window=20,
    )

    engine = BacktestEngine(
        strategy=strategy,
        initial_cash=100_000,
    )

    report = engine.run(
        df=df,
        symbol="MU",
    )

    assert report is not None

    assert report.initial_cash == 100_000

    assert report.final_equity > 0

    assert report.equity_curve is not None

    assert len(report.equity_curve.points) == len(df)
