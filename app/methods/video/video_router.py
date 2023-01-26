from fastapi import APIRouter
from .search import router as SearchRouter

router = APIRouter(prefix='/video')

router.include_router(SearchRouter)