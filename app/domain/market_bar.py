from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class MarketBar:

    symbol: str

    datetime: datetime

    interval: str

    open: float

    high: float

    low: float

    close: float

    volume: float
