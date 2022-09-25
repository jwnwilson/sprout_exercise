from typing import List
from xmlrpc.client import boolean

from pydantic import BaseModel


# DB DTO
class Post(BaseModel):
    title: str
    paragraphs: List[str]
    has_foul_language: boolean

# API DTO
class PostAPICreate(BaseModel):
    title: str
    paragraphs: List[str]
