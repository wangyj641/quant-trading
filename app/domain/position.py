from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Position:
    symbol: str

    quantity: int = 0

    entry_time: datetime = None

    average_price: float = 0.0

    market_price: float = 0.0

    @property
    def market_value(self) -> float:

        return self.quantity * self.market_price

    @property
    def unrealized_pnl(self) -> float:

        return self.quantity * (self.market_price - self.average_price)

    @property
    def cost(self) -> float:
        return self.quantity * self.average_price

    @property
    def is_empty(self) -> bool:
        return self.quantity == 0

    def buy(self, quantity: int, price: float):
        old_quantity = self.quantity

        old_cost = old_quantity * self.average_price

        new_cost = quantity * price

        total_quantity = old_quantity + quantity

        self.average_price = (old_cost + new_cost) / total_quantity

        self.quantity = total_quantity
