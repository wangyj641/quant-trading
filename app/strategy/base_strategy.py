from abc import ABC, abstractmethod
import pandas as pd

from app.domain.trading_signal import TradingSignal


class Strategy(ABC):

    @abstractmethod
    def generate(
        self,
        symbol: str,
        df: pd.DataFrame,
    ) -> list[TradingSignal]: ...
