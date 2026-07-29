from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Trade:

    symbol: str

    entry_time: datetime

    exit_time: datetime

    entry_price: float

    exit_price: float

    quantity: int

    profit: float

    return_pct: float

    def print(self):

        print("=" * 40)

        print(f"symbol        : {self.symbol}")
        print(f"entry_time    : {self.entry_time}")
        print(f"exit_time     : {self.exit_time}")
        print(f"quantity      : {self.quantity}")
        print(f"entry_price   : {self.entry_price:,.2f}")
        print(f"exit_price    : {self.exit_price:,.2f}")
        print(f"profit        : {self.profit:,.2f}")
        print(f"return_pct    : {self.return_pct:.2%}")
