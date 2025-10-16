from fastapi import FastAPI
from . import schema,services,profile
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.include_router(profile.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

