from dataclasses import dataclass

from app.backtest.equity_curve import EquityCurve
from app.domain.trade import Trade


@dataclass(slots=True)
class BacktestReport:

    initial_cash: float
    final_cash: float
    final_equity: float

    total_return: float

    max_drawdown: float
    volatility: float
    sharpe_ratio: float

    gross_profit: float
    gross_loss: float

    win_rate: float
    profit_factor: float

    trades: list[Trade]
    open_trades: list[Trade]

    equity_curve: EquityCurve
