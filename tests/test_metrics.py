from app.backtest.metrics import BacktestMetrics


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
