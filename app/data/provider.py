from abc import ABC, abstractmethod
import pandas as pd


class MarketDataProvider(ABC):
    """市场数据提供者接口"""

    @abstractmethod
    def download_history(
        self,
        symbol: str,
        period: str = "1y",
        interval: str = "1d",
    ) -> pd.DataFrame:
        """下载历史行情"""
        pass


    