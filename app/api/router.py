from fastapi import APIRouter

from app.routers import items
from app.routers import category_router

api_router = APIRouter()

api_router.include_router(
    items.router
)

api_router.include_router(
    category_router.router
)