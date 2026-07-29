from __future__ import annotations
from venv import logger

import pandas as pd

from app.execution.execution_result import ExecutionResult
from app.domain.trading_signal import TradingSignal, SignalType
from app.portfolio.portfolio import Portfolio


class BacktestExecution:

    def __init__(
        self,
        initial_cash: float = 100000,
    ):
        self.initial_cash = initial_cash

    def execute(
        self,
        df: pd.DataFrame,
        signals: list[TradingSignal],
    ) -> ExecutionResult:

        portfolio = Portfolio(self.initial_cash)

        signal_map = {signal.datetime: signal for signal in signals}

        for index, row in df.iterrows():

            signal = signal_map.get(index)

            if signal is None:
                continue

            price = float(row["close"])

            #
            # BUY
            #
            if signal.signal == SignalType.BUY:

                logger.info(f"Executing BUY signal for {signal.symbol} at {index}")

                quantity = int(portfolio.cash // price)

                if quantity > 0:

                    portfolio.buy(
                        symbol=signal.symbol,
                        price=price,
                        quantity=quantity,
                        datetime=index,
                    )

            #
            # SELL
            #
            elif signal.signal == SignalType.SELL:

                position = portfolio.get_position(signal.symbol)

                if position is not None and position.quantity > 0:

                    portfolio.sell(
                        symbol=signal.symbol,
                        price=price,
                        quantity=position.quantity,
                        datetime=index,
                    )

        return ExecutionResult(portfolio)
