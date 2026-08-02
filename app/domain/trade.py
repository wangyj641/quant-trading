from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Trade:

    symbol: str

    entry_datetime: datetime
    entry_price: float
    quantity: float

    exit_datetime: datetime | None = None
    exit_price: float | None = None

    pnl: float | None = None
    return_pct: float | None = None

    @property
    def is_closed(self) -> bool:
        return self.exit_datetime is not None

    @property
    def is_winner(self) -> bool:
        return self.is_closed and self.pnl is not None and self.pnl > 0

    @property
    def is_loser(self) -> bool:
        return self.is_closed and self.pnl is not None and self.pnl < 0

    def close(
        self,
        datetime: datetime,
        price: float,
    ) -> None:

        if self.is_closed:
            raise ValueError("Trade is already closed")

        self.exit_datetime = datetime
        self.exit_price = price

        self.pnl = (price - self.entry_price) * self.quantity

        if self.entry_price != 0:
            self.return_pct = (price - self.entry_price) / self.entry_price
        else:
            self.return_pct = 0.0
