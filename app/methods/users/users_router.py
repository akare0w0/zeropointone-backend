from fastapi import APIRouter
# 导入实际功能：login & regis
from .login import router as UserLoginRouter
from .regis import router as UserRegisRouter

router = APIRouter(prefix='/users')

router.include_router(UserLoginRouter)
router.include_router(UserRegisRouter)