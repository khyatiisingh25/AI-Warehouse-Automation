import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
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

MODEL_DIR = (
    BASE_DIR
    / "ai-core"
    / "models"
    / "saved"
)

MODEL_FILE = MODEL_DIR / "demand_model.pkl"


def train_model():
    # Load processed dataset
    df = pd.read_csv(DATA_FILE)

    # Create previous-day demand feature
    df["previous_demand"] = df["demand"].shift(1)

    # Remove first row
    df = df.dropna()

    # Feature used for training
    X = df[["previous_demand"]]

    # Target
    y = df["demand"]

    # Create and train model
    model = LinearRegression()
    model.fit(X, y)

    # Create model directory
    MODEL_DIR.mkdir(parents=True, exist_ok=True)

    # Save trained model
    joblib.dump(model, MODEL_FILE)

    print("Model trained successfully!")
    print(f"Model saved to: {MODEL_FILE}")
    print(f"Training rows: {len(X)}")


if __name__ == "__main__":
    train_model()