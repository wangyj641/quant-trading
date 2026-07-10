import yfinance as yf
import pandas as pd

from app.data.provider import MarketDataProvider


class YahooProvider(MarketDataProvider):

    def download_history(
        self,
        symbol: str,
        period: str = "1y",
        interval: str = "1d",
    ) -> pd.DataFrame:

        return yf.download(
            symbol,
            period=period,
            interval=interval,
            auto_adjust=True,
            progress=False,
        )