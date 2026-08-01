from abc import ABC, abstractmethod

import pandas as pd

from app.domain.trading_signal import TradingSignal


class Strategy(ABC):

    @abstractmethod
    def generate_signals(
        self,
        df: pd.DataFrame,
        symbol: str,
    ) -> list[TradingSignal]:
        pass
