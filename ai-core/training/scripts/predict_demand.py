import pandas as pd
from pathlib import Path
import joblib


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[3]

DATA_FILE = (
    BASE_DIR
    / "ai-core"
    / "datasets"
    / "processed"
    / "demand_processed.csv"
)

MODEL_FILE = (
    BASE_DIR
    / "ai-core"
    / "models"
    / "saved"
    / "demand_model.pkl"
)


def predict_next_demand():
    # Load trained model
    model = joblib.load(MODEL_FILE)

    # Load processed dataset
    df = pd.read_csv(DATA_FILE)

    # Get latest demand
    latest_demand = df["demand"].iloc[-1]

    # Create input using the same feature name used during training
    prediction_input = pd.DataFrame(
        {
            "previous_demand": [latest_demand]
        }
    )

    # Predict next-day demand
    prediction = model.predict(prediction_input)

    print("Latest demand:", latest_demand)
    print("Predicted next-day demand:", round(prediction[0], 2))


if __name__ == "__main__":
    predict_next_demand()