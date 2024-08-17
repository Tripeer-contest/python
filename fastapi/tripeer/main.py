from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from domain.crowing import router as crowing_router
from domain.tourapi import router as tourapi_router


app = FastAPI()

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

app.include_router(tourapi_router.router)
app.include_router(crowing_router.router)