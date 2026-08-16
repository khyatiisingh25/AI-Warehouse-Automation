from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_demand_prediction_api():
    response = client.post(
        "/api/v1/demand/predict",
        json={"previous_demand": 35},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["previous_demand"] == 35
    assert "predicted_next_day_demand" in data
    assert isinstance(data["predicted_next_day_demand"], float)


def test_demand_prediction_api_rejects_negative_demand():
    response = client.post(
        "/api/v1/demand/predict",
        json={"previous_demand": -5},
    )

    assert response.status_code == 422


def test_demand_prediction_api_rejects_invalid_demand():
    response = client.post(
        "/api/v1/demand/predict",
        json={"previous_demand": "invalid"},
    )

    assert response.status_code == 422