from typing import List
from app.schemas import Post, PostAPICreate
from sqlalchemy.orm import Session
import json

from .ml import analyse_sentences
from app.crud import post
from app.models import Post as PostModel


def parse_post_to_DTO(post_model: PostModel):
    return Post(
        title=post_model.title,
        paragraphs=json.loads(post_model.paragraphs),
        has_foul_language=post_model.has_foul_language
    )


def create_post(db: Session, *, post_obj: PostAPICreate) -> Post:
    """
    Analyse Post data object and return post data object
    """
    # Process process sentences in paragraphs
    results = analyse_sentences(post_obj)

    # check for foul language
    has_foul_language = any([r.has_foul_language for r in results])

    # Save results in DB
    new_post = Post(
        has_foul_language = has_foul_language,
        **post_obj.dict()
    ) 
    post_model = post.create(db, obj_in=new_post)
    return parse_post_to_DTO(post_model)


def get_posts(db: Session, *, skip: int = 0, limit: int = 100) -> List[Post]:
    post_data = post.get_multi(db, skip=skip, limit=limit)
    return [parse_post_to_DTO(post_model) for post_model in post_data]
