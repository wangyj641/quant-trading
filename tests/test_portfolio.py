from app.portfolio.portfolio import Portfolio
from datetime import datetime


def test_buy():
    portfolio = Portfolio(10000)

    portfolio.buy(
        symbol="MU",
        quantity=10,
        price=120,
        datetime=datetime(2026, 1, 1),
    )

    assert portfolio.cash == 8800

    position = portfolio.get_position("MU")

    assert position is not None
    assert position.quantity == 10
    assert position.average_price == 120


def test_average_price():

    portfolio = Portfolio(10000)

    portfolio.buy(
        "MU",
        10,
        120,
        datetime(2026, 1, 1),
    )

    portfolio.buy(
        "MU",
        10,
        130,
        datetime(2026, 1, 2),
    )

    position = portfolio.get_position("MU")

    assert position.quantity == 20
    assert position.average_price == 125


def test_sell():

    portfolio = Portfolio(10000)

    portfolio.buy(
        "MU",
        10,
        120,
        datetime(2026, 1, 1),
    )

    portfolio.sell(
        "MU",
        10,
        130,
        datetime(2026, 1, 2),
    )

    assert portfolio.cash == 10100

    assert portfolio.get_position("MU") is None

    assert len(portfolio.trades) == 1

    trade = portfolio.trades[0]

    assert trade.symbol == "MU"
    assert trade.entry_price == 120
    assert trade.exit_price == 130
    assert trade.quantity == 10
    assert trade.profit == 100


def test_partial_sell():

    portfolio = Portfolio(10000)

    portfolio.buy(
        "MU",
        10,
        120,
        datetime(2026, 1, 1),
    )

    portfolio.sell(
        "MU",
        4,
        130,
        datetime(2026, 1, 2),
    )

    position = portfolio.get_position("MU")

    assert position is not None
    assert position.quantity == 6

    assert len(portfolio.trades) == 0


def test_snapshot():

    portfolio = Portfolio(10000)

    portfolio.buy(
        "MU",
        10,
        120,
        datetime(2026, 1, 1),
    )

    snapshot = portfolio.snapshot(
        datetime(2026, 1, 2),
        {
            "MU": 130,
        },
    )

    assert snapshot.cash == 8800
    assert snapshot.market_value == 1300
    assert snapshot.total_value == 10100
