import pandas as pd

from app.backtest.engine import BacktestEngine
from app.domain.signal import Signal


def test_backtest():

    df = pd.DataFrame(
        {
            "close": [100, 105, 110],
            "signal": [
                Signal.BUY.value,
                Signal.HOLD.value,
                Signal.SELL.value,
            ],
        }
    )

    engine = BacktestEngine(initial_cash=100000)

    report = engine.run(df)

    assert report.trade_count == 1

    assert report.final_cash > 100000


def test_equity_curve():

    df = pd.DataFrame(
        {
            "close": [100, 110, 120],
            "signal": [Signal.BUY.value, Signal.HOLD.value, Signal.SELL.value],
        }
    )

    engine = BacktestEngine(initial_cash=10000)

    report = engine.run(df)

    assert len(report.equity_curve) == 3
