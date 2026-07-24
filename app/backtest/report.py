from dataclasses import dataclass

import pandas as pd

from app.backtest.trade import Trade


@dataclass(slots=True)
class BacktestReport:

    initial_cash: float

    final_cash: float

    total_return: float

    trade_count: int

    win_rate: float

    trades: list[Trade]

    # 新增：每日账户价值
    equity_curve: pd.Series
