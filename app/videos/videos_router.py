from fastapi import APIRouter
from .search_fuzz import router as SearchFuzzRouter
from .create_video   import router as AddVideoRouter

router = APIRouter(prefix='/videos')

router.include_router(SearchFuzzRouter)
router.include_router(AddVideoRouter)