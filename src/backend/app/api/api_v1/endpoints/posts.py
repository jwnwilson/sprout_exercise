from typing import Any

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
    post = logic.post.create(db=db, obj_in=post)
    return post
