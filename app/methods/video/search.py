from fastapi import APIRouter
from ...db.db import get_db

router = APIRouter(prefix='/search')

@router.get("/")
def search(keyword: str):
    pass