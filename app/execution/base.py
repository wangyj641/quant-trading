from abc import ABC, abstractmethod

import pandas as pd

from app.domain.trading_signal import TradingSignal
from app.execution.execution_result import ExecutionResult


class ExecutionEngine(ABC):

    @abstractmethod
    def execute(
        self,
        df: pd.DataFrame,
        signals: list[TradingSignal],
    ) -> ExecutionResult: ...
