from app.domain.position import Position
from app.domain.trade import Trade
from app.domain.transaction import Transaction
from app.portfolio.snapshot import PortfolioSnapshot


class Portfolio:

    def __init__(
        self,
        initial_cash: float,
    ):

        self.initial_cash = initial_cash

        self.cash = initial_cash

        self.positions: dict[str, Position] = {}

        self.transactions: list[Transaction] = []

        self.trades: list[Trade] = []

        self.snapshots: list[PortfolioSnapshot] = []

    @property
    def total_positions(self) -> int:
        return len(self.positions)

    def buy(
        self,
        symbol: str,
        price: float,
        quantity: int,
        datetime: int,
    ):

        cost = price * quantity

        if cost > self.cash:
            raise ValueError("Insufficient cash")

        self.cash -= cost

        position = self.positions.get(symbol)

        if position is None:

            self.positions[symbol] = Position(
                symbol=symbol,
                quantity=quantity,
                average_price=price,
            )

            position = self.positions.get(symbol)

        else:

            total_cost = position.average_price * position.quantity + cost

            total_quantity = position.quantity + quantity

            position.average_price = total_cost / total_quantity

            position.quantity = total_quantity

        return position

    def sell(
        self,
        symbol: str,
        price: float,
        quantity: int,
        datetime: int,
    ):

        position = self.positions[symbol]

        if quantity > position.quantity:
            raise ValueError("Not enough shares")

        self.cash += quantity * price

        position.quantity -= quantity

        if position.quantity == 0:
            del self.positions[symbol]

        # if the position is closed, we can calculate the profit and return percentage
        # create a trade object and add it to the trades list

    def get_position(
        self,
        symbol: str,
    ) -> Position | None:

        return self.positions.get(symbol)

    @property
    def invested_value(self):
        return sum(position.cost for position in self.positions.values())

    def snapshot(
        self,
        datetime,
        prices: dict[str, float],
    ): ...

    def summary(self):
        return {
            "cash": self.cash,
            "invested_value": self.invested_value,
            "total_value": self.cash + self.invested_value,
        }

    def total_value(
        self,
        prices,
    ):

        value = self.cash

        for symbol, position in self.positions.items():
            value += prices[symbol] * position.quantity

        return value
