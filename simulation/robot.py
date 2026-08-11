from dataclasses import dataclass

from simulation.models import Position


@dataclass
class Robot:
    """Represents a robot/AGV in the warehouse simulation."""

    robot_id: str
    position: Position

    def __post_init__(self) -> None:
        if not self.robot_id.strip():
            raise ValueError("robot_id cannot be empty.")

    def move_to(self, position: Position) -> None:
        """Update the robot's current position."""
        self.position = position