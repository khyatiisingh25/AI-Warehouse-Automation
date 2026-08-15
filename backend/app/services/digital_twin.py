"""
Service layer for exposing Digital Twin simulation state.

This module acts as an adapter between the simulation domain models
and the backend/API representation.

It does not contain FastAPI routes or database logic.
"""

from simulation.models import Position, Warehouse
from simulation.robot import Robot

from app.schemas.digital_twin import (
    PositionResponse,
    RobotStateResponse,
    WarehouseStateResponse,
)


class DigitalTwinStateService:
    """Convert simulation state into backend/API representations."""

    @staticmethod
    def position_to_response(
        position: Position,
    ) -> PositionResponse:
        """Convert a simulation Position into an API representation."""

        return PositionResponse(
            row=position.row,
            column=position.column,
        )

    @classmethod
    def robot_to_response(
        cls,
        robot: Robot,
    ) -> RobotStateResponse:
        """Convert a simulated Robot into an API representation."""

        return RobotStateResponse(
            robot_id=robot.robot_id,
            current_position=cls.position_to_response(
                robot.current_position
            ),
            target_position=(
                cls.position_to_response(robot.target_position)
                if robot.target_position is not None
                else None
            ),
            state=robot.state,
            route=[
                cls.position_to_response(position)
                for position in robot.route
            ],
        )

    @classmethod
    def warehouse_to_response(
        cls,
        warehouse: Warehouse,
        robots: list[Robot],
    ) -> WarehouseStateResponse:
        """
        Convert the current Digital Twin warehouse state
        and robots into a backend/API representation.
        """

        blocked_positions = [
            cls.position_to_response(shelf.position)
            for shelf in warehouse.shelves
        ]

        return WarehouseStateResponse(
            rows=warehouse.rows,
            columns=warehouse.columns,
            blocked_positions=blocked_positions,
            robots=[
                cls.robot_to_response(robot)
                for robot in robots
            ],
        )