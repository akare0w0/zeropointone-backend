# 常规导入 后面不再赘述
from fastapi import APIRouter

# 导入按功能区分的路由（不知道怎么形容才好）
from .users.users_router  import router as UsersRouter
from .videos.video_router import router as VideosRouter

# 创建一个新的路由
# prefix 前缀 就像localhost:8080/api的 /api就是前缀 根路由的/省略（合并）了
router = APIRouter(prefix='/api')

router.include_router(UsersRouter)
router.include_router(VideosRouter)