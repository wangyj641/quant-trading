from app.data.provider import MarketDataProvider


class IBKRProvider(MarketDataProvider):

    def download_history(
        self,
        symbol: str,
        period: str = "1y",
        interval: str = "1d",
    ):
        raise NotImplementedError()