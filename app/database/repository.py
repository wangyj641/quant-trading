from app.database.db import SessionLocal
from app.database.models import Price
from app.database.orm_mapper import ORMMapper


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
