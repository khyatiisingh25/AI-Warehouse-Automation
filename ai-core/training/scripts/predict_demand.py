import os
import joblib
import pandas as pd


MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "../../models/saved/demand_model.pkl"
)


def predict_next_day_demand(previous_demand):
    """
    Predict next-day demand using the trained model.

    Parameters:
        previous_demand (float): Most recent demand value.

    Returns:
        float: Predicted next-day demand.
    """

    model = joblib.load(MODEL_PATH)

    input_data = pd.DataFrame({
        "previous_demand": [previous_demand]
    })

    prediction = model.predict(input_data)

    return float(prediction[0])


if __name__ == "__main__":
    latest_demand = 35

    predicted_demand = predict_next_day_demand(latest_demand)

    print("Latest demand:", latest_demand)
    print("Predicted next-day demand:", round(predicted_demand, 2))