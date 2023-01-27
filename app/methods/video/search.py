from fastapi import APIRouter
from ...db.db import get_db
import jieba

router = APIRouter(prefix='/search_jieba')

@router.get("/abc")
def search(keyword: str):
    videosTitle = [] #视频标题
    keywords = " ".join(jieba.lcut(keyword, cut_all=True)).split(" ") #分割后的关键字
    for kw in keywords: #根据关键字搜索
        for i in range(10): #获取前十个视频的标题
            col = get_db().get_collection("video")
            videosTitle.append(col.find_one({"title":kw})) #将标题添加到列表中

    return videosTitle