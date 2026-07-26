from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class SignalType(Enum):
    BUY = "BUY"
    SELL = "SELL"


@dataclass(slots=True)
class TradingSignal:
    symbol: str
    datetime: datetime
    signal: SignalType
