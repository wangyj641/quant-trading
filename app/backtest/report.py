from dataclasses import dataclass

from app.domain.trade import Trade


@dataclass(slots=True)
class BacktestReport:

    initial_cash: float

    final_cash: float

    final_equity: float

    total_return: float

    trades: list[Trade]
