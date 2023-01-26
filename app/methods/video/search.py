from fastapi import APIRouter
from ...db.db import get_db

router = APIRouter(prefix='/search')

@router.get("/{keyword}")
def search(keyword: str):
    pass