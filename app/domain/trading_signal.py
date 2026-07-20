from dataclasses import dataclass
from datetime import datetime

from app.domain.signal import Signal


@dataclass(slots=True)
class TradingSignal:
    symbol: str
    datetime: datetime
    signal: Signal
    price: float
