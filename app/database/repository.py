from app.database.db import SessionLocal
from app.database.models import Price


class PriceRepository:

    def save(self, records):

        session = SessionLocal()

        for row in records:

            session.add(row)

        session.commit()

        session.close()