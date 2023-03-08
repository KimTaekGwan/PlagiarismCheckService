from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import api_image, api_xai, api_nlp, api_test

# 출처 명시
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]


def include_router(app):
    app.include_router(api_image.router, prefix='/image')
    app.include_router(api_xai.router, prefix='/xai')
    app.include_router(api_nlp.router, prefix='/nlp')
    app.include_router(api_test.router, prefix='/test')

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