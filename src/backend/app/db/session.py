from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def get_engine(database_uri=settings.SQLALCHEMY_DATABASE_URI):
    return create_engine(database_uri, pool_pre_ping=True)


def create_session(database_uri=settings.SQLALCHEMY_DATABASE_URI):
    engine = get_engine(database_uri)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal
