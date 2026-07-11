from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Index,
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Price(Base):

    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)

    symbol = Column(String(20), nullable=False)

    datetime = Column(DateTime, nullable=False)

    interval = Column(String(10), nullable=False)

    open = Column(Float)

    high = Column(Float)

    low = Column(Float)

    close = Column(Float)

    volume = Column(Float)

    __table_args__ = (
        Index(
            "idx_symbol_datetime_interval",
            "symbol",
            "datetime",
            "interval",
            unique=True,
        ),
    )