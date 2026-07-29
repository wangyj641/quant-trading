from app.portfolio.portfolio import Portfolio
from datetime import datetime


def test_portfolio():

    portfolio = Portfolio(100000)

    assert portfolio.cash == 100000
    assert portfolio.total_positions == 0

    portfolio.buy("MU", 100, 10, datetime.now())

    assert portfolio.cash == 99000

    position = portfolio.get_position("MU")

    assert position.quantity == 10

    portfolio.buy("MU", 120, 10, datetime.now())

    position = portfolio.get_position("MU")

    assert position.quantity == 20

    assert position.average_price == 110

    portfolio.sell(
        "MU",
        130,
        20,
        datetime.now(),
    )

    assert portfolio.total_positions == 0
