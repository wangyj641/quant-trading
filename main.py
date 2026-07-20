from app.config.settings import DATA_DIR, LOG_DIR
from app.data.downloader import Downloader
from app.data.provider_factory import create_provider

from app.database.repository import PriceRepository
from app.services.market_data_service import MarketDataService
from app.domain.timeframe import TimeFrame

from app.database.models import Base
from app.database.db import engine

from app.indicators.indicator_engine import IndicatorEngine

from app.indicators.ma_indicator import MAIndicator

from app.converters.dataframe_converter import DataFrameConverter
from app.strategy.ma_cross_strategy import MACrossStrategy


from pathlib import Path


def dellete_db():

    db = Path("data/market.db")

    if db.exists():
        db.unlink()


def test_strategy(repo):
    bars = repo.get_history(
        symbol="MU",
        timeFrame=TimeFrame.DAY_1,
        limit=300,
    )

    df = DataFrameConverter.bars_to_dataframe(bars)

    engine = IndicatorEngine()

    engine.register(MAIndicator(5))
    engine.register(MAIndicator(20))

    df = engine.calculate(df)

    strategy = MACrossStrategy()

    result = strategy.run(df)

    print(result.tail(20))


def main():
    print("Hello from quant-trading!")

    print("Data:", DATA_DIR)
    print("Logs:", LOG_DIR)

    dellete_db()

    Base.metadata.create_all(engine)

    provider = create_provider()

    downloader = Downloader(provider)
    repo = PriceRepository()

    service = MarketDataService(
        downloader,
        repo,
    )

    service.sync_symbol("MU")

    test_strategy(repo)

    repo.close()


if __name__ == "__main__":
    main()
