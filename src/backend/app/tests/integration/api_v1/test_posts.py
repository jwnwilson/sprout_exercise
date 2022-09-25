from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
import pytest
import json

from app.core.config import settings
from app.models.post import Post


@pytest.fixture()
def post_instance(db: Session) -> Post:
    post = Post(
        title="test",
        paragraphs=json.dumps(['test']),
        has_foul_language=False
    )
    db.add(post)
    db.commit()
    yield post


def test_create_post_no_foul_language(
    client: TestClient, db: Session
) -> None:
    data = {"title": "Foo", "paragraphs": ["test"]}
    response = client.post(
        f"{settings.API_V1_STR}/posts/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["paragraphs"] == data["paragraphs"]
    assert content["has_foul_language"] == False


def test_create_post_foul_language(
    client: TestClient, db: Session
) -> None:
    data = {"title": "Foo", "paragraphs": ["shit"]}
    response = client.post(
        f"{settings.API_V1_STR}/posts/", json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["title"] == data["title"]
    assert content["paragraphs"] == data["paragraphs"]
    assert content["has_foul_language"] == True


def test_read_posts(
    client: TestClient, db: Session, post_instance
) -> None:
    response = client.get(
        f"{settings.API_V1_STR}/posts/"
    )
    assert response.status_code == 200
    content = response.json()
    assert content[0]["title"] == post_instance.title
    assert content[0]["paragraphs"] == json.loads(post_instance.paragraphs)
    assert content[0]["has_foul_language"] == post_instance.has_foul_language
