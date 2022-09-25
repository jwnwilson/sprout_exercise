from typing import Generator
from app.db.session import create_session


def get_db() -> Generator:
    try:
        SessionLocal = create_session()
        db = SessionLocal()
        yield db
    finally:
        db.close()
