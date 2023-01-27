from fastapi import APIRouter
from ...db.db import get_client

router = APIRouter(prefix='/search_fuzz')

@router.get("/")
def search_fuzz(keyword: str):
    pass