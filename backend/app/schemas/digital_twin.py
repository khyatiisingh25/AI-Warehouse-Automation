"""
Backend/API representation of Digital Twin simulation state.

This module defines the data contract consumed by the backend/API layer.
It does not contain simulation logic.
"""

from pydantic import BaseModel, ConfigDict

from simulation.robot import RobotState


class PositionResponse(BaseModel):
    """API representation of a warehouse grid position."""

    row: int
    column: int


class RobotStateResponse(BaseModel):
    """Backend-facing representation of a simulated robot."""

    model_config = ConfigDict(use_enum_values=True)

    robot_id: str
    current_position: PositionResponse
    target_position: PositionResponse | None = None
    state: RobotState
    route: list[PositionResponse] = []


class WarehouseStateResponse(BaseModel):
    """Backend-facing representation of the Digital Twin warehouse."""

    rows: int
    columns: int
    blocked_positions: list[PositionResponse]
    robots: list[RobotStateResponse]