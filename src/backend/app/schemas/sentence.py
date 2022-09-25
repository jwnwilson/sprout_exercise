from typing import List

from pydantic import BaseModel


# Oppurtunity for sharing DTOs across projects with shared library
class Sentence(BaseModel):
    fragment: str


class SentenceResponse(BaseModel):
    hasFoulLanguage: bool