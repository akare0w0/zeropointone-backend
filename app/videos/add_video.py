from fastapi import APIRouter
from typing import List, Any
from pymongo.typings import *

router = APIRouter(prefix='/add')

@router.post('/')
def add_video(
    title: str,
    author: str,
    upload_time: object,
    video_url: str,
    video_tags: List[Any],
):
    pass