from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import json

from app.crud.base import CRUDBase
from app.models.post import Post
from app.schemas.post import Post as PostDTO


class CRUDPost(CRUDBase[Post, PostDTO]):
    def create(
        self, db: Session, *, obj_in: PostDTO
    ) -> Post:
        obj_in_data = jsonable_encoder(obj_in)
        # convert list of str to text
        obj_in_data["paragraphs"] = json.dumps(
            obj_in_data["paragraphs"]
        )
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

post = CRUDPost(Post)
