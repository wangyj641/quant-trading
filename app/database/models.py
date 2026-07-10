from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Price(Base):

    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)

    symbol = Column(String)

    date = Column(String)

    open = Column(Float)

    high = Column(Float)

    low = Column(Float)

    close = Column(Float)

    volume = Column(Float)