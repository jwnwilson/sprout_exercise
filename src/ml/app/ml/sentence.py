from app.schemas import SentenceResponse

def analyse_sentence(sentence) -> SentenceResponse:
    return SentenceResponse(has_foul_language=False)