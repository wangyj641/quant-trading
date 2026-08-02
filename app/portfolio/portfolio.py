from sqlalchemy.util import symbol

from app.domain.position import Position
from app.domain.trade import Trade
from app.domain.transaction import Transaction
from app.portfolio.snapshot import PortfolioSnapshot
from datetime import datetime
from app.domain.transaction import TransactionSide


class Portfolio:

    def __init__(
        self,
        initial_cash: float,
    ):

        self.initial_cash = initial_cash

        self.cash = initial_cash

        self.positions: dict[str, Position] = {}

        self.transactions: list[Transaction] = []

        self.trades: list[Trade] = []

        self.snapshots: list[PortfolioSnapshot] = []

        self.open_trades: dict[str, Trade] = {}

    @property
    def total_positions(self) -> int:
        return len(self.positions)

    def _add_position(
        self,
        symbol: str,
        quantity: int,
        price: float,
    ):
        position = self.positions.get(symbol)

        if position is None:

            self.positions[symbol] = Position(
                symbol=symbol,
                quantity=quantity,
                average_price=price,
                entry_time=datetime.now(),
            )
            return

        position.buy(quantity, price)

    def _remove_position(
        self,
        symbol: str,
        quantity: int,
        price: float,
        datetime: datetime,
    ):
        position = self.positions[symbol]

        if quantity < position.quantity:

            position.quantity -= quantity

            return

        self._close_position(
            position=position,
            exit_price=price,
            exit_time=datetime,
        )

        del self.positions[symbol]

    def _close_position(
        self,
        position: Position,
        exit_price: float,
        exit_time: datetime,
    ):
        profit = (exit_price - position.average_price) * position.quantity

        return_pct = (exit_price - position.average_price) / position.average_price

        trade = Trade(
            symbol=position.symbol,
            entry_datetime=position.entry_time,
            exit_datetime=exit_time,
            entry_price=position.average_price,
            exit_price=exit_price,
            quantity=position.quantity,
            pnl=profit,
            return_pct=return_pct,
        )

        self.trades.append(trade)

    def buy(
        self,
        symbol: str,
        quantity: int,
        price: float,
        datetime: datetime,
        commission: float = 0.0,
    ):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if price <= 0:
            raise ValueError("Price must be positive")

        if commission < 0:
            raise ValueError("Commission cannot be negative")

        total_cost = quantity * price + commission

        if total_cost > self.cash:
            raise ValueError("Insufficient cash")

        self.cash -= total_cost

        transaction = Transaction(
            symbol=symbol,
            datetime=datetime,
            side=TransactionSide.BUY,
            quantity=quantity,
            price=price,
            commission=commission,
        )

        self.transactions.append(transaction)

        self._add_position(
            symbol=symbol,
            quantity=quantity,
            price=price,
        )

    def sell(
        self,
        symbol: str,
        quantity: int,
        price: float,
        datetime: datetime,
        commission: float = 0.0,
    ):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if price <= 0:
            raise ValueError("Price must be positive")

        position = self.positions.get(symbol)

        if position is None:
            raise ValueError(f"No position for {symbol}")

        if quantity > position.quantity:
            raise ValueError(f"Not enough shares of {symbol}")

        proceeds = quantity * price - commission

        self.cash += proceeds

        transaction = Transaction(
            symbol=symbol,
            datetime=datetime,
            side=TransactionSide.SELL,
            quantity=quantity,
            price=price,
            commission=commission,
        )

        self.transactions.append(transaction)

        self._remove_position(
            symbol=symbol,
            quantity=quantity,
            price=price,
            datetime=datetime,
        )

    def get_position(
        self,
        symbol: str,
    ) -> Position | None:

        return self.positions.get(symbol)

    @property
    def invested_value(self):
        return sum(position.cost for position in self.positions.values())

    def summary(self):
        return {
            "cash": self.cash,
            "invested_value": self.invested_value,
            "total_value": self.cash + self.invested_value,
        }

    def total_value(
        self,
        prices: dict[str, float],
    ) -> float:

        value = self.cash

        for symbol, position in self.positions.items():

            if symbol not in prices:
                raise ValueError(f"Missing price for {symbol}")

            value += position.quantity * prices[symbol]

        return value

    def snapshot(
        self,
        datetime: datetime,
        prices: dict[str, float],
    ) -> PortfolioSnapshot:

        market_value = 0.0

        for symbol, position in self.positions.items():

            if symbol not in prices:
                raise ValueError(f"Missing price for {symbol}")

            market_value += position.quantity * prices[symbol]

        total_value = self.cash + market_value

        snapshot = PortfolioSnapshot(
            datetime=datetime,
            cash=self.cash,
            market_value=market_value,
            total_value=total_value,
        )

        self.snapshots.append(snapshot)

        return snapshot
