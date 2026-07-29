from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class PortfolioSnapshot:

    datetime: datetime

    cash: float

    market_value: float

    total_value: float
