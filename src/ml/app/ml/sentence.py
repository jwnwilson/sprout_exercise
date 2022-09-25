from app.schemas import SentenceResponse

from profanity_filter import ProfanityFilter


def analyse_sentence(sentence) -> SentenceResponse:
    pf = ProfanityFilter()
    has_foul_language = pf.is_clean(sentence.fragment)

    return SentenceResponse(has_foul_language=has_foul_language)