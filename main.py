from app.config.settings import DATA_DIR, LOG_DIR
from app.data.downloader import Downloader
from app.data.provider_factory import create_provider

from app.database.repository import PriceRepository
from app.services.market_data_service import MarketDataService

from app.database.models import Base
from app.database.db import engine


def main():
    print("Hello from quant-trading!")

    print("Data:", DATA_DIR)
    print("Logs:", LOG_DIR)

    Base.metadata.create_all(engine)

    provider = create_provider()

    downloader = Downloader(provider)
    repo = PriceRepository()

    service = MarketDataService(
        downloader,
        repo,
    )

    service.sync_symbol("MU")

    repo.close()


if __name__ == "__main__":
    main()
