from app.config.settings import DATA_DIR, LOG_DIR
from app.data.downloader import Downloader
from app.data.provider_factory import create_provider
from app.data.mapper import PriceMapper
from app.database.repository import PriceRepository

from app.database.models import Base
from app.database.db import engine

import pandas as pd


def main():
    print("Hello from quant-trading!")

    print("Data:", DATA_DIR)
    print("Logs:", LOG_DIR)

    Base.metadata.create_all(engine)



    provider = create_provider()

    downloader = Downloader(provider)

    df = downloader.download(
        "MU",
        period="5y",
    )

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    prices = PriceMapper.from_dataframe(
        df,
        "MU",
        "1d",
    )

    repo = PriceRepository()

    repo.save_all(prices)

    repo.close()



if __name__ == "__main__":
    main()
