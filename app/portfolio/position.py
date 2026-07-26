from dataclasses import dataclass


@dataclass(slots=True)
class Position:
    symbol: str
    quantity: int = 0
    average_price: float = 0.0

    @property
    def market_value(self) -> float:
        return self.quantity * self.average_price
