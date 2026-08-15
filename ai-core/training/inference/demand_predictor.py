from pathlib import Path

import joblib
import pandas as pd


MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "saved"
    / "demand_model.pkl"
)


def predict_next_day_demand(previous_demand):
    """
    Predict next-day demand using the trained demand model.

    Parameters:
        previous_demand (float): Most recent demand value.

    Returns:
        float: Predicted next-day demand.
    """
    model = joblib.load(MODEL_PATH)

    input_data = pd.DataFrame(
        {
            "previous_demand": [previous_demand]
        }
    )

    prediction = model.predict(input_data)

    return float(prediction[0])