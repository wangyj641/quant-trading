from datetime import datetime

from app.backtest.equity_curve import EquityCurve


def test_equity_curve():

    curve = EquityCurve()

    curve.add(
        datetime(2026, 1, 1),
        100_000,
    )

    curve.add(
        datetime(2026, 1, 2),
        105_000,
    )

    curve.add(
        datetime(2026, 1, 3),
        102_000,
    )

    assert curve.initial_value == 100_000

    assert curve.final_value == 102_000

    assert curve.values == [
        100_000,
        105_000,
        102_000,
    ]
