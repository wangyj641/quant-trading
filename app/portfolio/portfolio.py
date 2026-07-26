from app.portfolio.position import Position


class Portfolio:

    def __init__(self, initial_cash: float):

        self.cash = initial_cash

        self.positions: dict[str, Position] = {}

    @property
    def total_positions(self) -> int:
        return len(self.positions)

    def buy(
        self,
        symbol: str,
        price: float,
        quantity: int,
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
    ):

        position = self.positions[symbol]

        if quantity > position.quantity:
            raise ValueError("Not enough shares")

        self.cash += quantity * price

        position.quantity -= quantity

        if position.quantity == 0:
            del self.positions[symbol]

    def get_position(
        self,
        symbol: str,
    ) -> Position | None:

        return self.positions.get(symbol)

    @property
    def invested_value(self):
        return sum(position.cost for position in self.positions.values())
