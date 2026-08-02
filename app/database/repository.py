from app.database.db import SessionLocal
from app.database.models import Price
from app.database.orm_mapper import ORMMapper
from app.domain.market_bar import MarketBar
from app.domain.timeframe import TimeFrame
from datetime import datetime

from sqlalchemy import select
import pandas as pd

from sqlalchemy import text


class PriceRepository:

    def __init__(self):

        self.session = SessionLocal()

    def save_all(self, bars):

        prices = [ORMMapper.to_price(bar) for bar in bars]

        self.session.add_all(prices)

        self.session.commit()

    def close(self):

        self.session.close()

    def get_latest_datetime(
        self,
        symbol,
        interval,
    ):

        stmt = select(func.max(Price.datetime)).where(
            Price.symbol == symbol,
            Price.interval == interval,
        )

        return self.session.scalar(stmt)

    def count(
        self,
        symbol,
        interval,
    ):

        stmt = select(func.count()).where(
            Price.symbol == symbol,
            Price.interval == interval,
        )

        return self.session.scalar(stmt)

    def get_history(
        self,
        symbol: str,
        timeframe: TimeFrame,
        start: datetime | None = None,
        end: datetime | None = None,
    ) -> pd.DataFrame:

        sql = """
            SELECT
                datetime,
                open,
                high,
                low,
                close,
                volume
            FROM prices
            WHERE symbol = :symbol
              AND interval = :interval
        """

        params = {
            "symbol": symbol,
            "interval": timeframe.value,
        }

        if start is not None:
            sql += """
                AND datetime >= :start
            """
            params["start"] = start

        if end is not None:
            sql += """
                AND datetime <= :end
            """
            params["end"] = end

        sql += """
            ORDER BY datetime ASC
        """

        result = self.session.execute(
            text(sql),
            params,
        )

        rows = result.fetchall()

        df = pd.DataFrame(
            rows,
            columns=result.keys(),
        )

        if df.empty:
            return df

        df["datetime"] = pd.to_datetime(df["datetime"])

        numeric_columns = [
            "open",
            "high",
            "low",
            "close",
            "volume",
        ]

        for column in numeric_columns:
            df[column] = pd.to_numeric(
                df[column],
                errors="coerce",
            )

        df = df.set_index("datetime")

        df = df.sort_index()

        return df
