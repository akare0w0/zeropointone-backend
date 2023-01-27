from fastapi import APIRouter
from .search_fuzz import router as SearchFuzzRouter

router = APIRouter(prefix='/video')

router.include_router(SearchFuzzRouter)