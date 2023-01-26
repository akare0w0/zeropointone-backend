# 结构差不多 不赘述
from fastapi import APIRouter
from .users.users_router import router as UsersRouter
from .video.video_router import router as VideoRouter

router = APIRouter(prefix='/methods')

router.include_router(UsersRouter)
router.include_router(VideoRouter)