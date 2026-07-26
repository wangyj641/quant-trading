from dataclasses import dataclass

from app.backtest.trade import Trade


@dataclass(slots=True)
class ExecutionResult:
    cash: float
    shares: int
    trades: list[Trade]
