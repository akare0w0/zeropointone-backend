from fastapi import APIRouter
from functools import cmp_to_key
from ..db.db import get_client
from ..db.data_filter import split_words, fuzzy_match

router = APIRouter(prefix='/search_fuzz')

@router.get("/")
def search_fuzz(keyword: str):
    keywords = split_words(keyword)
    if keywords == list():
        keywords = [keyword]

    def cmp_time(a, b):
        if  a['upload_time']['year'] > b['upload_time']['year'] or \
            a['upload_time']['month'] > b['upload_time']['month'] or \
            a['upload_time']['day'] > b['upload_time']['day']:
            return 1
        elif a['upload_time']['year'] == b['upload_time']['year'] or \
             a['upload_time']['month'] == b['upload_time']['month'] or \
             a['upload_time']['day'] == b['upload_time']['day']:
            return 0
        else:
            return -1
    def cmp_ratio(a, b):
        if a['ratio'] > b['ratio']:
            return 1
        elif a['ratio'] == b['ratio']:
            return 0
        else:
            return -1

    result = {
        'videos': [],
    }
    
    videos = []
    client = get_client()
    db_videos = client.get_database('videos').get_collection('videos').find({}, { '_id': 0 })
    db_users  = client.get_database('users').get_collection('users')

    # 查找视频
    for video in db_videos.limit(30):
        videos.append(video)

    # 根据视频发布时间排序，越晚的越前
    videos.sort(key=cmp_to_key(cmp_time), reverse=True)

    ratios = [0 for i in range(len(videos))]
    ratios_count = 0
    i = 0
    for video in videos:
        for keyword in keywords:
            ratios[i] += fuzzy_match(keyword, video['title'])
            ratios_count += 1
        ratios[i] = ratios[i] / (1 if ratios_count == 0 else ratios_count)
        ratios_count = 0
        i += 1

    result_videos = []

    for ratio, video in zip(ratios, videos):
        if ratio > 0:
            title = video['title']
            author = video['author']
            upload_time = video['upload_time']
            video_url = video['video_url']
            author = db_users.find_one({ '_id': author })['nickname']
            result_videos.append(dict(title=title, author=author, upload_time=upload_time, video_url=video_url, ratio=ratio))

    result['videos'] = sorted(result_videos, key=cmp_to_key(cmp_ratio), reverse=True)

    return result