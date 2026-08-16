import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.api import digital_twin

from simulation.digital_twin import create_default_simulation


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_simulation(monkeypatch):
    """Give every API test a fresh simulation state."""

    monkeypatch.setattr(
        digital_twin,
        "simulation",
        create_default_simulation(),
    )


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

    assert len(robot["route"]) > 0

    assert robot["route"][0] == {
        "row": 0,
        "column": 0,
    }

    assert robot["route"][-1] == {
        "row": 4,
        "column": 4,
    }

    for position in robot["route"]:
        assert "row" in position
        assert "column" in position


def test_digital_twin_empty_robot_case(monkeypatch):
    simulation = create_default_simulation()
    simulation.robots = []

    monkeypatch.setattr(
        digital_twin,
        "simulation",
        simulation,
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


def test_digital_twin_step_endpoint_returns_200():
    response = client.post("/api/v1/digital-twin/step")

    assert response.status_code == 200


def test_digital_twin_step_updates_robot_position():
    response = client.post("/api/v1/digital-twin/step")

    assert response.status_code == 200

    data = response.json()

    assert len(data["robots"]) == 1

    robot = data["robots"][0]

    assert robot["robot_id"] == "R1"

    assert robot["current_position"] != {
        "row": 0,
        "column": 0,
    }

    assert robot["state"] == "MOVING"


def test_digital_twin_state_reflects_latest_simulation():
    step_response = client.post(
        "/api/v1/digital-twin/step"
    )

    assert step_response.status_code == 200

    step_data = step_response.json()

    state_response = client.get(
        "/api/v1/digital-twin/state"
    )

    assert state_response.status_code == 200

    state_data = state_response.json()

    assert (
        state_data["robots"][0]["current_position"]
        == step_data["robots"][0]["current_position"]
    )

    assert (
        state_data["robots"][0]["state"]
        == step_data["robots"][0]["state"]
    )