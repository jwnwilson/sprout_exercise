from typing import Any, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import logic, schemas
from app.api import deps

router = APIRouter()


@router.post("/", response_model=schemas.Post)
def create_post(
    *,
    db: Session = Depends(deps.get_db),
    post: schemas.PostAPICreate,
) -> Any:
    """
    Create new post and filter it for prophanity.
    """
    post = logic.create_post(db=db, post_obj=post)
    return post


@router.get("/", response_model=List[schemas.Post])
def read_items(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100
) -> Any:
    """
    Retrieve items.
    """
    posts = logic.get_posts(db=db, skip=skip, limit=limit)
    return posts
