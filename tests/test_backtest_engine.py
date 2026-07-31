from datetime import datetime

import pandas as pd

from app.backtest.engine import BacktestEngine
from app.domain.trading_signal import (
    TradingSignal,
    SignalType,
)


def test_backtest_engine():

    index = pd.to_datetime(
        [
            "2026-01-01",
            "2026-01-02",
        ]
    )

    df = pd.DataFrame(
        {
            "close": [
                100.0,
                110.0,
            ]
        },
        index=index,
    )

    signals = [
        TradingSignal(
            symbol="MU",
            datetime=index[0],
            signal=SignalType.BUY,
        ),
        TradingSignal(
            symbol="MU",
            datetime=index[1],
            signal=SignalType.SELL,
        ),
    ]

    engine = BacktestEngine(initial_cash=10_000)

    report = engine.run(
        df=df,
        signals=signals,
        symbol="MU",
    )

    assert report.initial_cash == 10_000

    assert report.final_cash == 11_000

    assert report.final_equity == 11_000

    assert report.total_return == 0.10

    assert len(report.trades) == 1
