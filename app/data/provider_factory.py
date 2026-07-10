from app.config.settings import DATA_PROVIDER, DataProviderType
from app.data.yahoo_provider import YahooProvider
from app.data.ibkr_provider import IBKRProvider


def create_provider():
    if DATA_PROVIDER == DataProviderType.YAHOO:
        return YahooProvider()

    if DATA_PROVIDER == DataProviderType.IBKR:
        return IBKRProvider()

    raise ValueError(f"Unsupported provider: {DATA_PROVIDER}")