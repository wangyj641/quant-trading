from app.database.db import SessionLocal
from app.database.models import Price


class PriceRepository:

    def __init__(self):

        self.session = SessionLocal()

    def save_all(self, prices):

        self.session.add_all(prices)

        self.session.commit()

    def close(self):

        self.session.close()