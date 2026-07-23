# app/backtest/report.py

from dataclasses import dataclass


@dataclass(slots=True)
class BacktestReport:

    initial_cash: float

    final_cash: float

    total_return: float

    trade_count: int

    win_rate: float
