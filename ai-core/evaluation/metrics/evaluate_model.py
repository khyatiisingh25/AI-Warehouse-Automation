import pandas as pd
from pathlib import Path
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error


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


def evaluate_model():
    # Load trained model
    model = joblib.load(MODEL_FILE)

    # Load processed dataset
    df = pd.read_csv(DATA_FILE)

    # Create previous-day demand feature
    df["previous_demand"] = df["demand"].shift(1)

    # Remove first row
    df = df.dropna()

    # Use the same feature name used during training
    X = df[["previous_demand"]]

    # Actual demand
    y = df["demand"]

    # Generate predictions
    predictions = model.predict(X)

    # Calculate metrics
    mae = mean_absolute_error(y, predictions)
    rmse = mean_squared_error(y, predictions) ** 0.5

    print("Model Evaluation")
    print("----------------")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")


if __name__ == "__main__":
    evaluate_model()