from app.portfolio.portfolio import Portfolio
from datetime import datetime


def test_buy():
    portfolio = Portfolio(100_000)

    portfolio.buy(
        symbol="MU",
        quantity=100,
        price=120,
        datetime=datetime(2026, 1, 1),
    )

    assert portfolio.cash == 88_000

    position = portfolio.get_position("MU")

    assert position is not None
    assert position.quantity == 100
    assert position.average_price == 120


def test_average_price():

    portfolio = Portfolio(100_000)

    portfolio.buy(
        "MU",
        100,
        120,
        datetime(2026, 1, 1),
    )

    portfolio.buy(
        "MU",
        100,
        130,
        datetime(2026, 1, 2),
    )

    position = portfolio.get_position("MU")

    assert position.quantity == 200
    assert position.average_price == 125


def test_sell():

    portfolio = Portfolio(100_000)

    portfolio.buy(
        "MU",
        100,
        120,
        datetime(2026, 1, 1),
    )

    portfolio.sell(
        "MU",
        100,
        130,
        datetime(2026, 1, 2),
    )

    assert portfolio.cash == 101_000

    assert portfolio.get_position("MU") is None

    assert len(portfolio.trades) == 1

    trade = portfolio.trades[0]

    assert trade.symbol == "MU"
    assert trade.entry_price == 120
    assert trade.exit_price == 130
    assert trade.quantity == 100
    assert trade.profit == 1_000


def test_partial_sell():

    portfolio = Portfolio(100_000)

    portfolio.buy(
        "MU",
        100,
        120,
        datetime(2026, 1, 1),
    )

    portfolio.sell(
        "MU",
        40,
        130,
        datetime(2026, 1, 2),
    )

    position = portfolio.get_position("MU")

    assert position is not None
    assert position.quantity == 60

    assert len(portfolio.trades) == 0


def test_snapshot():

    portfolio = Portfolio(100_000)

    portfolio.buy(
        "MU",
        100,
        120,
        datetime(2026, 1, 1),
    )

    snapshot = portfolio.snapshot(
        datetime(2026, 1, 2),
        {
            "MU": 130,
        },
    )

    assert snapshot.cash == 88_000
    assert snapshot.market_value == 13_000
    assert snapshot.total_value == 101_000
