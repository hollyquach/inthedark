import os 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import oauth

app = FastAPI()

app.include_router(oauth.router)

origins = [
    os.environ.get("CORS_HOST", "http://localhost"),
    os.getenv('CORE_URI')
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)