from typing import Dict, Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import create_session, get_engine
from app.main import app


@pytest.fixture(autouse=True)
def test_db():
    from app.db.base_class import Base
    Base.metadata.create_all(bind=get_engine())
    yield
    Base.metadata.drop_all(bind=get_engine())

@pytest.fixture(scope="session")
def db() -> Generator:
    SessionLocal = create_session()
    yield SessionLocal()


@pytest.fixture(scope="module")
def client() -> Generator:
    with TestClient(app) as c:
        yield c
