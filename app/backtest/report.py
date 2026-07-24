from dataclasses import dataclass
from app.backtest.trade import Trade
from pandas import Series


@dataclass(slots=True)
class BacktestReport:

    initial_cash: float
    final_cash: float

    total_return: float

    trade_count: int
    win_rate: float

    trades: list[Trade]
