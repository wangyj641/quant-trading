from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Trade:
    entry_time: datetime
    exit_time: datetime

    entry_price: float
    exit_price: float

    quantity: int

    profit: float
    return_pct: float
