from typing import Generator
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def get_db() -> Generator:
    try:
        db = Session(engine)
        yield db
    finally:
        db.close()