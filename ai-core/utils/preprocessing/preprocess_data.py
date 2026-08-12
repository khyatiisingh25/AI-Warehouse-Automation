import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parents[2]

RAW_FILE = BASE_DIR / "datasets" / "raw" / "sample_demand.csv"
PROCESSED_DIR = BASE_DIR / "datasets" / "processed"
PROCESSED_FILE = PROCESSED_DIR / "demand_processed.csv"


def preprocess_data():
    # Load raw dataset
    df = pd.read_csv(RAW_FILE)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"])

    # Sort data by product and date
    df = df.sort_values(["product_id", "date"])

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove invalid demand values
    df = df[df["demand"] >= 0]

    # Create processed directory if needed
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    # Save processed dataset
    df.to_csv(PROCESSED_FILE, index=False)

    print(f"Processed dataset saved to: {PROCESSED_FILE}")
    print(f"Rows: {len(df)}")


if __name__ == "__main__":
    preprocess_data()