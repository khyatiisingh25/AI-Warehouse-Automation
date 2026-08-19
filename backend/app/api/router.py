from fastapi import APIRouter

from app.api.auth import router as auth_router
from app.api.detection import router as detection_router
from app.api.inventory import router as inventory_router
from app.api.products import router as products_router
from app.api.shelves import router as shelves_router


api_router = APIRouter()

api_router.include_router(detection_router)
api_router.include_router(products_router)
api_router.include_router(inventory_router)
api_router.include_router(shelves_router)
api_router.include_router(auth_router)