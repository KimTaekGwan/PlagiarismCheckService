from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_get, api_post, gpu_test, py_test

# 출처 명시
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


def include_router(app):
    app.include_router(api_get.router, prefix='/get')
    app.include_router(api_post.router, prefix='/main')
    app.include_router(gpu_test.router, prefix='/ai')
    app.include_router(py_test.router, prefix='/test')

def start_application():
    app = FastAPI()
    include_router(app)
    return app


app = start_application()

# 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)