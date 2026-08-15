"""
Robot/AGV simulation model for the warehouse Digital Twin.

This module contains simulation-only robot state and movement logic.
It does not depend on FastAPI, PostgreSQL, or frontend code.
"""

from dataclasses import dataclass, field
from enum import Enum

from simulation.models import Position
from simulation.pathfinding import AStarPathfinder


class RobotState(str, Enum):
    """Possible states of a warehouse robot/AGV."""

    IDLE = "IDLE"
    MOVING = "MOVING"
    WAITING = "WAITING"
    BLOCKED = "BLOCKED"
    COMPLETED = "COMPLETED"


@dataclass
class Robot:
    """Represents a robot/AGV in the warehouse simulation."""

    robot_id: str
    current_position: Position

    target_position: Position | None = None
    route: list[Position] = field(default_factory=list)
    state: RobotState = RobotState.IDLE

    def __post_init__(self) -> None:
        if not self.robot_id.strip():
            raise ValueError("robot_id cannot be empty.")

    @property
    def position(self) -> Position:
        """Backward-compatible access to the robot's current position."""

        return self.current_position

    def move_to(self, position: Position) -> None:
        """Move the robot directly to a position."""

        self.current_position = position

    def set_target(self, target: Position) -> None:
        """Set the robot's target position."""

        self.target_position = target
        self.route = []
        self.state = RobotState.IDLE

    def calculate_route(
        self,
        pathfinder: AStarPathfinder,
    ) -> list[Position] | None:
        """Calculate a route from current position to target."""

        if self.target_position is None:
            raise ValueError("Robot target position is not set.")

        try:
            path = pathfinder.find_path(
                self.current_position,
                self.target_position,
            )
        except ValueError:
            self.route = []
            self.state = RobotState.BLOCKED
            return None

        if path is None:
            self.route = []
            self.state = RobotState.BLOCKED
            return None

        self.route = path

        if self.current_position == self.target_position:
            self.state = RobotState.COMPLETED
        else:
            self.state = RobotState.MOVING

        return self.route

    def move_next(self) -> bool:
        """Move the robot to the next position in its calculated route."""

        if self.target_position is None:
            self.state = RobotState.IDLE
            return False

        if self.current_position == self.target_position:
            self.state = RobotState.COMPLETED
            self.route = []
            return False

        if not self.route:
            self.state = RobotState.WAITING
            return False

        if self.route[0] == self.current_position:
            self.route.pop(0)

        if not self.route:
            self.state = RobotState.COMPLETED
            return False

        self.current_position = self.route.pop(0)

        if self.current_position == self.target_position:
            self.state = RobotState.COMPLETED
        else:
            self.state = RobotState.MOVING

        return True

    def block(self) -> None:
        """Mark the robot as blocked by a dynamic obstacle."""

        self.state = RobotState.BLOCKED

    def wait(self) -> None:
        """Put the robot into a waiting state."""

        self.state = RobotState.WAITING

    def reset(self) -> None:
        """Reset the robot to its idle state."""

        self.target_position = None
        self.route = []
        self.state = RobotState.IDLE