from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from app.core.config import settings
from app.api.router import api_router
from app.core.lifespan import lifespan
from app.core.logging import configure_logging
from app.exceptions.exceptions import AppException
from app.routers import items

from app.exceptions.handlers import (
    app_exception_handler,
    http_exception_handler,
    validation_exception_handler
)

configure_logging()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan,
)

app.include_router(api_router)

app.add_exception_handler(
    AppException,
    app_exception_handler,
)

app.add_exception_handler(
    HTTPException,
    http_exception_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_exception_handler,
)


@app.get("/")
async def read_root():
    return {
        "message": "Inventory Management API running!"
    }