from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DemandPredictionResult:
    product_id: str
    predicted_demand: float


class DemandPredictionService:
    """Predict future product demand from historical quantities."""

    def predict(
        self,
        product_id: str,
        historical_demand: list[float],
    ) -> DemandPredictionResult:
        if not product_id.strip():
            raise ValueError("product_id cannot be empty.")

        if not historical_demand:
            raise ValueError("Historical demand cannot be empty.")

        if any(value < 0 for value in historical_demand):
            raise ValueError("Demand values cannot be negative.")

        predicted_demand = sum(historical_demand) / len(historical_demand)

        return DemandPredictionResult(
            product_id=product_id,
            predicted_demand=predicted_demand,
        )