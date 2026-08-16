from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

from fastapi import APIRouter

from app.schemas.demand import (
    DemandPredictionRequest,
    DemandPredictionResponse,
)


PROJECT_ROOT = Path(__file__).resolve().parents[3]

PREDICTOR_PATH = (
    PROJECT_ROOT
    / "ai-core"
    / "training"
    / "inference"
    / "demand_predictor.py"
)

spec = spec_from_file_location(
    "demand_predictor",
    PREDICTOR_PATH,
)

if spec is None or spec.loader is None:
    raise ImportError(
        f"Could not load demand predictor from {PREDICTOR_PATH}"
    )

demand_predictor = module_from_spec(spec)
spec.loader.exec_module(demand_predictor)

predict_next_day_demand = demand_predictor.predict_next_day_demand


router = APIRouter(
    prefix="/demand",
    tags=["Demand Prediction"],
)


@router.post(
    "/predict",
    response_model=DemandPredictionResponse,
)
def predict_demand(
    request: DemandPredictionRequest,
) -> DemandPredictionResponse:
    predicted_demand = predict_next_day_demand(
        request.previous_demand
    )

    return DemandPredictionResponse(
        previous_demand=request.previous_demand,
        predicted_next_day_demand=float(predicted_demand),
    )