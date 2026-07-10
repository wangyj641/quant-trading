from app.data.provider import MarketDataProvider


class Downloader:

    def __init__(self, provider: MarketDataProvider):
        self.provider = provider

    def download(
        self,
        symbol: str,
        period: str = "1y",
        interval: str = "1d",
    ):

        return self.provider.download_history(
            symbol,
            period,
            interval,
        )