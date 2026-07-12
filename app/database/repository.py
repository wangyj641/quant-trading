from app.database.db import SessionLocal
from app.database.models import Price
from app.database.orm_mapper import ORMMapper

from sqlalchemy import select


from app.domain.market_bar import MarketBar

from app.domain.timeframe import TimeFrame


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
        symbol,
        timeFrame: TimeFrame,
        limit: int | None = None,
    ) -> list[MarketBar]:

        stmt = (
            select(Price)
            .where(
                Price.symbol == symbol,
                Price.interval == timeFrame.value,
            )
            .order_by(Price.datetime.asc())
        )

        if limit:
            stmt = stmt.limit(limit)

        prices = self.session.scalars(stmt).all()

        return [ORMMapper.to_market_bar(price) for price in prices]
