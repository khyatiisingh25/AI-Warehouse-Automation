from app.schemas.digital_twin import (
    PositionResponse,
    RobotStateResponse,
    WarehouseStateResponse,
)
from app.services.digital_twin import DigitalTwinStateService

from simulation.models import Position, Shelf, Warehouse
from simulation.robot import Robot, RobotState


def test_position_to_response():
    position = Position(2, 3)

    result = DigitalTwinStateService.position_to_response(position)

    assert isinstance(result, PositionResponse)
    assert result.row == 2
    assert result.column == 3


def test_robot_to_response():
    robot = Robot(
        "R1",
        Position(0, 0),
    )

    robot.set_target(Position(4, 4))
    robot.route = [
        Position(0, 0),
        Position(0, 1),
        Position(1, 1),
        Position(4, 4),
    ]
    robot.state = RobotState.MOVING

    result = DigitalTwinStateService.robot_to_response(robot)

    assert isinstance(result, RobotStateResponse)

    assert result.robot_id == "R1"

    assert result.current_position.row == 0
    assert result.current_position.column == 0

    assert result.target_position is not None
    assert result.target_position.row == 4
    assert result.target_position.column == 4

    assert result.state == RobotState.MOVING

    assert len(result.route) == 4


def test_robot_without_target():
    robot = Robot(
        "R1",
        Position(1, 2),
    )

    result = DigitalTwinStateService.robot_to_response(robot)

    assert result.robot_id == "R1"
    assert result.target_position is None
    assert result.state == RobotState.IDLE
    assert result.route == []


def test_warehouse_to_response():
    warehouse = Warehouse(5, 5)

    warehouse.add_shelf(
        Shelf(
            shelf_id="S1",
            shelf_code="SHELF-001",
            zone="A",
            rack="R1",
            level=1,
            max_capacity=100,
            position=Position(2, 2),
        )
    )

    robot = Robot(
        "R1",
        Position(0, 0),
    )

    robot.set_target(Position(4, 4))
    robot.state = RobotState.MOVING

    result = DigitalTwinStateService.warehouse_to_response(
        warehouse,
        [robot],
    )

    assert isinstance(result, WarehouseStateResponse)

    assert result.rows == 5
    assert result.columns == 5

    assert len(result.blocked_positions) == 1
    assert result.blocked_positions[0].row == 2
    assert result.blocked_positions[0].column == 2

    assert len(result.robots) == 1
    assert result.robots[0].robot_id == "R1"
    assert result.robots[0].state == RobotState.MOVING