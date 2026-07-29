from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class TransactionSide(StrEnum):
    BUY = "BUY"
    SELL = "SELL"


@dataclass(slots=True)
class Transaction:
    symbol: str
    datetime: datetime
    side: TransactionSide
    quantity: int
    price: float
    commission: float = 0.0

    @property
    def value(self) -> float:
        return self.quantity * self.price
