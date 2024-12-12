from fastapi import FastAPI
from app.api.V1.routers import Router as V1_Router
from app.core.db import Base,engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(V1_Router, prefix="/api/v1")


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
