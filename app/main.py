from fastapi import FastAPI
from . import models
from .database import engine
from app.routers import post, user, auth, vote
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

from fastapi.testclient import TestClient

# # при каждом запуске будут отслеживатся все изменения в models и автоматически запускать изменения в бд
# # но тк у нас есть  alembic,то мы закоментируем это

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/')
def hello():
    return {'message':'Hello world'}

