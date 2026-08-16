from pydantic import BaseModel, Field


class DemandPredictionRequest(BaseModel):
    previous_demand: float = Field(ge=0)


class DemandPredictionResponse(BaseModel):
    previous_demand: float
    predicted_next_day_demand: float