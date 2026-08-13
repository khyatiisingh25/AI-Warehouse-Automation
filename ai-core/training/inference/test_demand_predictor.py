import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from demand_predictor import predict_next_day_demand


def test_predict_next_day_demand():
    prediction = predict_next_day_demand(35)

    assert isinstance(prediction, float)
    assert prediction >= 0


if __name__ == "__main__":
    test_predict_next_day_demand()
    print("Test passed")