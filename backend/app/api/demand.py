from fastapi import APIRouter

from ai_core.training.inference.demand_predictor import (
    predict_next_day_demand,
)

from app.schemas.demand import (
    DemandPredictionRequest,
    DemandPredictionResponse,
)


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