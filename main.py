# 替代命令行的uvicorn指令 直接用python main.py运行
from uvicorn import run
# 导入fastapi
from fastapi import FastAPI
# 导入中间件
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
# 导入根路由
from app.root_router import router as RootRouter
# 创建fastapi的实例
app = FastAPI()
# 感兴趣可以查一下 CORS
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 将根路由添加到app的路由中
app.include_router(RootRouter)

# @app.exception_handler(StarletteHTTPException)
# def exception_handler(request, exc):
    # return RedirectResponse("/api/404")

if __name__ == '__main__':
    run('main:app', host='0.0.0.0', port=8080, reload=True)