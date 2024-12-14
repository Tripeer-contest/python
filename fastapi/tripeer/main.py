from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.middleware.cors import CORSMiddleware

from domain.trend import router as trend_router
from domain.crowing import router as crowing_router
from domain.tourapi import router as tourapi_router
from domain.recommend import router as recommend_router
from domain.elasticsearch import router as elasticsearch_router
from domain.tourapi.scheduler import scheduler as tourapi_scheduler

@asynccontextmanager
async def lifespan(app):
    tourapi_scheduler.start()
    yield

app = FastAPI(lifespan=lifespan)

origins = [
    "http://127.0.0.1:8080",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(trend_router.router)
app.include_router(crowing_router.router)
app.include_router(tourapi_router.router)
app.include_router(recommend_router.router)
app.include_router(elasticsearch_router.router)
