from fastapi import APIRouter, UploadFile
from typing import List, Any
from datetime import datetime
from os.path import abspath
from ..db.db import get_client
from ..db.data_filter import is_vaild_strs

router = APIRouter(prefix='/create')

@router.post('/')
def create_video(
    title: str,
    author: str,
    video: UploadFile = None,
    front_cover: UploadFile = None,
    video_tags: List[Any] = list(),
    upload_time: dict = dict(
        year   = datetime.now().year,
        month  = datetime.now().day,
        hour   = datetime.now().hour,
        minute = datetime.now().minute,
    ),
):
    result = {
        'vaild': True,
        'success': True,
    }

    client = get_client()
    db_videos = client.get_database('videos').get_collection('videos')
    db_users  = client.get_database('users').get_collection('users')

    if not is_vaild_strs((title, author)) or not is_vaild_strs(video_tags):
        result['vaild'] = False
    else:
        id = db_videos.insert_one({
            'title': title,
            'author': author,
            'upload_time': upload_time,
            'video_url': '',
            'front_cover_url': '', 
            'video_tags': video_tags,
            'video_comments': [],
        }).inserted_id

        author = db_users.find_one({ '_id': author })
        author['video'].append()

        path = abspath('..')
        vid_path = f'/locals/videos/{id}.{video.filename.split(".")[-1]}'
        front_cover_path = f'/locals/front_cover/{id}.{front_cover.filename.split(".")[-1]}'

        with open(path + vid_path, 'wb') as f:
            f.write(video.read())
        with open(path + front_cover_path, 'wb') as f:
            f.write(front_cover.read())

        result['success'] = True

    return result