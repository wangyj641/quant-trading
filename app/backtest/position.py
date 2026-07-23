from dataclasses import dataclass


@dataclass
class Position:

    quantity: int = 0

    entry_price: float = 0

    cash: float = 100000
