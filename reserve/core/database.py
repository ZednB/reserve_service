from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from reserve.core.config import settings

SQLALCHEMY_DATABASE_URL = str(settings.POSTGRES_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from reserve.models.table import Table
from reserve.models.reservation import Reservation
print(f"Зарегистрированные таблицы: {Base.metadata.tables.keys()}")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
