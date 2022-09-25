from typing import List

from pydantic import BaseModel


# Opportunity for sharing DTOs across projects with shared library
class Sentence(BaseModel):
    fragment: str


class SentenceResponse(BaseModel):
    has_foul_language: bool