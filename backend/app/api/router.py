from fastapi import APIRouter

from app.api.detection import router as detection_router
from app.api.digital_twin import router as digital_twin_router


api_router = APIRouter()

api_router.include_router(detection_router)
api_router.include_router(digital_twin_router)