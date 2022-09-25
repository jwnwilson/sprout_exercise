from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Post(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    paragraphs = Column(Text)
    has_foul_language = Column(Boolean, nullable=True)

