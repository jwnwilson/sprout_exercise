from app.schemas import Post
from sqlalchemy.orm import Session

from .ml_api import analyse_sentences
from crud import post


def create(db: Session, *, post_obj: Post) -> Post:
    """
    Analyse Post data object and return post data object
    """
    # Process process sentences in paragraphs
    results = analyse_sentences(post_obj)

    # check for foul language
    has_foul_language = any([r["has_foul_language"] for r in results])

    post_obj.has_foul_language = has_foul_language

    # Save results in DB
    post.create(db, post)

    return post

