import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from scripts.constants import AppSpec
from scripts.db import init_db
from scripts.services import router

app = FastAPI(
    title=AppSpec.name,
    description=AppSpec.description,
    summary=AppSpec.summary,
)

if os.environ.get("ENABLE_CORS") in (True, "true", "True") and os.environ.get("CORS_URLS"):
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["GET", "POST", "DELETE", "PUT"],
        allow_headers=["*"],
    )

app.include_router(router)

@app.on_event("startup")
def on_startup():
    init_db()
