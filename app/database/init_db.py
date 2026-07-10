from app.database.db import engine
from app.database.models import Base


def init_database():

    Base.metadata.create_all(engine)