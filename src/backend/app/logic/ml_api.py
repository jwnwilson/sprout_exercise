import requests
from typing import List
from pydantic import ValidationError
from schemas import Sentence, SentenceResponse, Post

ML_API_ENDPOINT = 'http://localhost:5001'

class ML_Exception(Exception):
    pass


def analyse_sentences(post_obj: Post) -> List[SentenceResponse]:
    sentences = []
    results = []

    for paragraph in post_obj.paragraphs:
        sentences = sentences + paragraph.split('.')

    for sentence in sentences:
        result = analyse_sentence(sentence)
        results.append(result)
    
    return results


def analyse_sentence(sentence: str) -> SentenceResponse:
    url = ML_API_ENDPOINT + '/sentence'

    # Validate date before sending
    sentence = Sentence(
        fragment = sentence
    )

    resp = requests.post(url, data=sentence.dict())

    if resp.status_code != 200:
        raise ML_Exception(f"Unable to retrieve ML result: {resp.text}")
    
    try:
        return SentenceResponse(**resp.json())
    except ValidationError as err:
        raise ML_Exception(f"Unable to parse ML result: {err}")  
