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
    assert trade.pnl == 100


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


def test_mark_to_market():

    portfolio = Portfolio(initial_cash=100_000)

    portfolio.buy(
        symbol="MU",
        datetime=datetime(2026, 1, 1),
        price=100,
        quantity=100,
    )

    equity = portfolio.mark_to_market(prices={"MU": 120})

    assert equity == 102_000


def test_daily_equity_curve():

    portfolio = Portfolio(initial_cash=100_000)

    equity_values = []

    portfolio.buy(
        symbol="MU",
        datetime=datetime(2026, 1, 1),
        price=100,
        quantity=100,
    )

    prices = [100, 110, 120, 90]

    for price in prices:

        equity = portfolio.mark_to_market(prices={"MU": price})

        equity_values.append(equity)

    assert len(equity_values) == 4

    assert equity_values == [
        100_000,
        101_000,
        102_000,
        99_000,
    ]
