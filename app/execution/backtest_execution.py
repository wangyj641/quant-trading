from __future__ import annotations

import pandas as pd

from app.domain.trading_signal import (
    TradingSignal,
    SignalType,
)
from app.execution.execution_result import ExecutionResult
from app.portfolio.portfolio import Portfolio
from app.constants.common import COMMISSION_RATE


class BacktestExecution:

    def __init__(
        self,
        initial_cash: float = 10000,
    ):
        self.initial_cash = initial_cash

    def execute(
        self,
        df: pd.DataFrame,
        signals: list[TradingSignal],
        symbol: str,
    ) -> ExecutionResult:

        portfolio = Portfolio(initial_cash=self.initial_cash)

        signal_map = {signal.datetime: signal for signal in signals}

        for index, row in df.iterrows():

            price = float(row["close"])

            signal = signal_map.get(index)

            if signal is not None:

                self._execute_signal(
                    portfolio=portfolio,
                    signal=signal,
                    price=price,
                    datetime=index,
                )

            portfolio.snapshot(
                datetime=index,
                prices={symbol: price},
            )

        return ExecutionResult(portfolio)

    def _execute_signal(
        self,
        portfolio: Portfolio,
        signal: TradingSignal,
        price: float,
        datetime,
    ) -> None:

        if signal.signal == SignalType.BUY:

            self._buy(
                portfolio,
                signal,
                price,
                datetime,
            )

        elif signal.signal == SignalType.SELL:

            self._sell(
                portfolio,
                signal,
                price,
                datetime,
            )

    def _buy(
        self,
        portfolio: Portfolio,
        signal: TradingSignal,
        price: float,
        datetime,
    ) -> None:

        quantity = int(portfolio.cash // price)

        if quantity <= 0:
            return

        portfolio.buy(
            symbol=signal.symbol,
            quantity=quantity,
            price=price,
            datetime=datetime,
            commission=COMMISSION_RATE,
        )

    def _sell(
        self,
        portfolio: Portfolio,
        signal: TradingSignal,
        price: float,
        datetime,
    ) -> None:

        position = portfolio.get_position(signal.symbol)

        if position is None:
            return

        if position.quantity <= 0:
            return

        portfolio.sell(
            symbol=signal.symbol,
            quantity=position.quantity,
            price=price,
            datetime=datetime,
            commission=COMMISSION_RATE,
        )
