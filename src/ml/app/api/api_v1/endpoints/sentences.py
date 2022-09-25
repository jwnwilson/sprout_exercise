from typing import Any

from fastapi import APIRouter

from app import ml, schemas

router = APIRouter()


@router.post("/", response_model=schemas.SentenceResponse)
def sentence_check(
    *,
    sentence: schemas.Sentence,
) -> Any:
    """
    Check sentence for traits
    """
    traits = ml.analyse_sentence(sentence)
    return traits
