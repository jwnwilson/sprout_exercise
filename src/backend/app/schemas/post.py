from typing import List
from xmlrpc.client import boolean

from pydantic import BaseModel


# Base DTO
class Post(BaseModel):
    title: str
    paragraphs: List[str]
    has_foul_language: boolean


# DB DTO
class PostDB(BaseModel):
    title: str
    paragraphs: str
    has_foul_language: boolean


# API DTO
class PostAPICreate(BaseModel):
    title: str
    paragraphs: List[str]
