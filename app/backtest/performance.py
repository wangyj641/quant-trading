from dataclasses import dataclass


@dataclass
class Performance:

    total_return: float

    trade_count: int

    win_rate: float

    max_drawdown: float
