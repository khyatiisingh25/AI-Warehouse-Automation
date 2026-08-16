from fastapi.testclient import TestClient

from app.main import app
from app.api import digital_twin


client = TestClient(app)


def test_digital_twin_endpoint_returns_200():
    response = client.get("/api/v1/digital-twin/state")

    assert response.status_code == 200


def test_digital_twin_response_schema():
    response = client.get("/api/v1/digital-twin/state")

    assert response.status_code == 200

    data = response.json()

    assert "rows" in data
    assert "columns" in data
    assert "blocked_positions" in data
    assert "robots" in data

    assert isinstance(data["rows"], int)
    assert isinstance(data["columns"], int)
    assert isinstance(data["blocked_positions"], list)
    assert isinstance(data["robots"], list)


def test_digital_twin_robot_state():
    response = client.get("/api/v1/digital-twin/state")

    assert response.status_code == 200

    data = response.json()

    assert len(data["robots"]) == 1

    robot = data["robots"][0]

    assert robot["robot_id"] == "R1"
    assert robot["state"] == "MOVING"

    assert robot["current_position"] == {
        "row": 0,
        "column": 0,
    }

    assert robot["target_position"] == {
        "row": 4,
        "column": 4,
    }


def test_digital_twin_positions_are_serialized():
    response = client.get("/api/v1/digital-twin/state")

    assert response.status_code == 200

    data = response.json()

    assert data["blocked_positions"] == [
        {
            "row": 2,
            "column": 2,
        }
    ]

    robot = data["robots"][0]

    assert robot["route"] == [
        {
            "row": 0,
            "column": 0,
        },
        {
            "row": 0,
            "column": 1,
        },
        {
            "row": 1,
            "column": 1,
        },
        {
            "row": 4,
            "column": 4,
        },
    ]


def test_digital_twin_empty_robot_case(monkeypatch):
    monkeypatch.setattr(
        digital_twin,
        "robots",
        [],
    )

    response = client.get("/api/v1/digital-twin/state")

    assert response.status_code == 200

    data = response.json()

    assert data["rows"] == 5
    assert data["columns"] == 5
    assert data["blocked_positions"] == [
        {
            "row": 2,
            "column": 2,
        }
    ]
    assert data["robots"] == []