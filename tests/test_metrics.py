from app.backtest.metrics import BacktestMetrics
from app.domain.trade import Trade
from datetime import datetime


def test_max_drawdown():

    values = [
        100_000,
        110_000,
        105_000,
        120_000,
    ]

    result = BacktestMetrics.max_drawdown(values)

    assert round(result, 4) == -0.0455


def test_total_return():

    result = BacktestMetrics.total_return(
        100_000,
        110_000,
    )

    assert result == 0.10


def test_volatility():

    values = [
        100,
        102,
        101,
        105,
        103,
    ]

    result = BacktestMetrics.volatility(values)

    assert result > 0


def test_sharpe_ratio():

    values = [
        100,
        102,
        104,
        106,
        108,
    ]

    result = BacktestMetrics.sharpe_ratio(values)

    assert result > 0


def make_trade(
    entry: float,
    exit: float,
    quantity: float = 100,
):

    trade = Trade(
        symbol="MU",
        entry_datetime=datetime(2026, 1, 1),
        entry_price=entry,
        quantity=quantity,
    )

    trade.close(
        datetime=datetime(2026, 1, 10),
        price=exit,
    )

    return trade


def test_win_rate():

    trades = [
        make_trade(100, 120),
        make_trade(100, 110),
        make_trade(100, 90),
        make_trade(100, 80),
    ]

    result = BacktestMetrics.win_rate(trades)

    assert result == 0.5


def test_profit_factor():

    trades = [
        make_trade(100, 120),
        make_trade(100, 110),
        make_trade(100, 90),
        make_trade(100, 80),
    ]

    result = BacktestMetrics.profit_factor(trades)

    assert result == 1.0
