from datetime import datetime

from app.domain.trade import Trade


def test_trade_lifecycle():

    trade = Trade(
        symbol="MU",
        entry_datetime=datetime(2026, 1, 1),
        entry_price=100,
        quantity=100,
    )

    assert trade.is_closed is False

    trade.close(
        datetime=datetime(2026, 1, 10),
        price=120,
    )

    assert trade.is_closed is True

    assert trade.exit_price == 120

    assert trade.pnl == 2000

    assert trade.return_pct == 0.20

    assert trade.is_winner is True

    assert trade.is_loser is False


def test_losing_trade():

    trade = Trade(
        symbol="MU",
        entry_datetime=datetime(2026, 1, 1),
        entry_price=100,
        quantity=100,
    )

    trade.close(
        datetime=datetime(2026, 1, 10),
        price=90,
    )

    assert trade.pnl == -1000

    assert trade.return_pct == -0.10

    assert trade.is_winner is False

    assert trade.is_loser is True
