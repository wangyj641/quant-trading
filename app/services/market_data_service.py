import pandas as pd
import turtle

from app.data.downloader import Downloader
from app.database.repository import PriceRepository
from app.data.mapper import PriceMapper


class MarketDataService:

    def __init__(
        self,
        downloader: Downloader,
        repository: PriceRepository,
    ):
        self.downloader = downloader
        self.repository = repository

    def sync_symbol(
        self,
        symbol,
        period="5y",
        interval="1d",
    ):

        df = self.downloader.download(
            symbol,
            period,
            interval,
        )

        # print(df.columns)

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        bars = PriceMapper.from_dataframe(
            df,
            symbol,
            interval,
        )

        self.repository.save_all(bars)

        print(f"{symbol}: saved {len(bars)} rows")
