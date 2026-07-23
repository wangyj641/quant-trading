from dataclasses import dataclass


@dataclass(slots=True)
class Position:

    symbol: str

    quantity: int = 0

    average_price: float = 0
