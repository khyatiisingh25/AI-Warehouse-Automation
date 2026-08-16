from fastapi import APIRouter

from app.api.detection import router as detection_router
from app.api.demand import router as demand_router


api_router = APIRouter()

api_router.include_router(detection_router)
api_router.include_router(demand_router)