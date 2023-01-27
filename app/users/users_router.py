from fastapi import APIRouter
# 导入实际功能：login & regis
from .login    import router as LoginRouter
from .register import router as RegisRouter

router = APIRouter(prefix='/users')

router.include_router(LoginRouter)
router.include_router(RegisRouter)