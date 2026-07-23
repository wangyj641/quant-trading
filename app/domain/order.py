from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OrderSide(Enum):
    BUY = "BUY"
    SELL = "SELL"


@dataclass(slots=True)
class Order:

    symbol: str

    side: OrderSide

    quantity: int

    price: float

    datetime: datetime
