from __future__ import annotations

import pandas as pd

from app.execution.base import ExecutionEngine
from app.execution.execution_result import ExecutionResult
from app.backtest.trade import Trade
from app.domain.trading_signal import SignalType
from app.backtest.metrics import Metrics


class BacktestExecution(ExecutionEngine):

    def __init__(
        self,
        initial_cash: float = 100000,
    ):
        self.initial_cash = initial_cash

    def execute(
        self,
        df: pd.DataFrame,
        signals,
    ) -> ExecutionResult:

        cash = self.initial_cash
        shares = 0

        # 暂时把 BacktestEngine 中
        # 买卖逻辑移动到这里

        cash = self.initial_cash
        shares = 0

        entry_price = 0.0
        entry_time = None

        trades = []

        equity_curve = []

        # 方便按照日期快速查找信号
        signal_map = {signal.datetime: signal for signal in signals}

        for index, row in df.iterrows():

            signal = signal_map.get(index, None)
            price = row["close"]

            portfolio_value = cash + shares * price

            equity_curve.append({"datetime": index, "value": portfolio_value})

            # BUY
            if signal == SignalType.BUY and shares == 0:

                shares = int(cash // price)

                if shares == 0:
                    continue

                cash -= shares * price

                entry_price = price
                entry_time = index

            # SELL
            elif signal == SignalType.SELL and shares > 0:

                cash += shares * price

                profit = (price - entry_price) * shares

                trades.append(
                    Trade(
                        entry_time=entry_time,
                        exit_time=index,
                        entry_price=entry_price,
                        exit_price=price,
                        quantity=shares,
                        profit=profit,
                        return_pct=(price - entry_price) / entry_price,
                    )
                )

                shares = 0

        # 最后一根K线仍然持仓
        if shares > 0:

            last_price = df.iloc[-1]["close"]

            cash += shares * last_price

            profit = (last_price - entry_price) * shares

            trades.append(
                Trade(
                    entry_time=entry_time,
                    exit_time=df.index[-1],
                    entry_price=entry_price,
                    exit_price=last_price,
                    quantity=shares,
                    profit=profit,
                    return_pct=(last_price - entry_price) / entry_price,
                )
            )

        trade_count = len(trades)

        win_count = len([t for t in trades if t.profit > 0])

        win_rate = win_count / trade_count if trade_count > 0 else 0

        total_return = (cash - self.initial_cash) / self.initial_cash

        equity_df = pd.DataFrame(equity_curve)

        equity_series = equity_df.set_index("datetime")["value"]

        max_drawdown = Metrics.max_drawdown(equity_series)

        return ExecutionResult(
            cash=cash,
            shares=shares,
            trades=trades,
        )
