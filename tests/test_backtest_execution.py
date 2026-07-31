from datetime import datetime

import pandas as pd

from app.execution.backtest_execution import (
    BacktestExecution,
)
from app.domain.trading_signal import (
    TradingSignal,
    SignalType,
)


def test_buy_signal():

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
        )
    ]

    execution = BacktestExecution(initial_cash=10000)

    result = execution.execute(
        df=df,
        signals=signals,
        symbol="MU",
    )

    portfolio = result.portfolio

    position = portfolio.get_position("MU")

    assert position is not None
    assert position.quantity == 100

    assert portfolio.cash == 0


def test_buy_sell():

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

    execution = BacktestExecution(initial_cash=10000)

    result = execution.execute(
        df=df,
        signals=signals,
        symbol="MU",
    )

    portfolio = result.portfolio

    assert portfolio.cash == 11000

    assert portfolio.get_position("MU") is None

    assert len(portfolio.trades) == 1
