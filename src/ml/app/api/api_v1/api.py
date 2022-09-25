from fastapi import APIRouter

from app.api.api_v1.endpoints import sentences

api_router = APIRouter()
api_router.include_router(sentences.router, prefix="/sentence", tags=["sentence"])
