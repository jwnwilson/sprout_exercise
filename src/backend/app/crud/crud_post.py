from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import PostCreate


class CRUDPost(CRUDBase[Post, Post]):
    def create(
        self, db: Session, *, obj_in: Post
    ) -> Post:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


post = CRUDPost(Post)
