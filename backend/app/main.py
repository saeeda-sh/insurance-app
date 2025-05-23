from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .utils.config import settings
from .routers import policy

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.CLIENT_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(policy.router, tags=["policies"], prefix="/api/policies")
