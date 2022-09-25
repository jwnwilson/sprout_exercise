from typing import List
from pydantic import ValidationError
from concurrent.futures import as_completed
from requests_futures.sessions import FuturesSession
from requests import Response

from app.schemas import Sentence, SentenceResponse, Post

ML_API_ENDPOINT = 'http://ml:5001/api/v1'
# Allow 20 async connections
request_session = FuturesSession()

class MLException(Exception):
    pass


def get_sentence_data(sentences: List[str], retries=3) -> List[SentenceResponse]:
    """
    Asynchronously get sentences analysis from the ML service with retry mechanism
    for requests that fail. Fail after 3 retries. 
    """
    url = ML_API_ENDPOINT + '/sentence'
    failures = []
    success = []
    responses = []

    for sentence in sentences:
        # Validate date before sending
        sentence = Sentence(
            fragment = sentence
        )
        future = request_session.post(url, json=sentence.dict())
        future.sentence = sentence
        responses.append(
            future
        )

    for future in as_completed(responses):
        resp = future.result()
        if resp.status_code == 200:
            success.append(SentenceResponse(**resp.json()))
        else:
            failures.append(future.sentence)
    
    if failures and retries > 0:
        success = success + get_sentence_data(failures, retries=retries-1)
    elif failures:
        raise MLException(f"Unable to retrieve ML results: {resp.text}")

    return success


def analyse_sentences(post_obj: Post) -> List[SentenceResponse]:
    sentences = []
    results = []

    # Get sentences from paragraphs
    for paragraph in post_obj.paragraphs:
        sentences = sentences + paragraph.split('.')

    # make async requests to ML api to speed up processing
    results = get_sentence_data(sentences)
    
    return results
