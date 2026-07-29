from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Position:
    symbol: str

    quantity: int = 0

    entry_time: datetime = None

    average_price: float = 0.0

    @property
    def cost(self) -> float:
        return self.quantity * self.average_price

    @property
    def is_empty(self) -> bool:
        return self.quantity == 0
