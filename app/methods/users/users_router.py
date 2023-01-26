from fastapi import APIRouter
# 导入实际功能：login & regis
from .login import router as UserLoginRouter

router = APIRouter(prefix='/users')

router.include_router(UserLoginRouter)