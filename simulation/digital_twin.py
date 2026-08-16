"""
Digital Twin simulation orchestration.

This module owns the live in-memory warehouse simulation state.
It coordinates WarehouseManager, A* pathfinding, and Robot movement.

It does not depend on FastAPI, PostgreSQL, or frontend code.
"""

from __future__ import annotations

from simulation.models import Position, Shelf, Warehouse
from simulation.pathfinding import AStarPathfinder
from simulation.robot import Robot, RobotState
from simulation.warehouse import WarehouseManager


class DigitalTwinSimulation:
    """Manage and advance the live Digital Twin simulation."""

    def __init__(
        self,
        warehouse: Warehouse,
        robots: list[Robot],
    ) -> None:
        self.warehouse_manager = WarehouseManager(warehouse)
        self.robots = robots
        self.pathfinder = AStarPathfinder(self.warehouse_manager)
        self.running = False

    @property
    def warehouse(self) -> Warehouse:
        """Return the underlying warehouse model."""

        return self.warehouse_manager.warehouse

    def start(self) -> None:
        """Start the Digital Twin simulation."""

        self.running = True

        for robot in self.robots:
            if (
                robot.target_position is not None
                and robot.state == RobotState.IDLE
            ):
                robot.calculate_route(self.pathfinder)


    def reset(self) -> None:
        """Reset the simulation to its initial state."""

        self.warehouse_manager = WarehouseManager(
            Warehouse(rows=5, columns=5)
        )

        self.warehouse_manager.add_shelf(
            Shelf(
                shelf_id="S1",
                position=Position(2, 2),
            )
        )

        self.robots = [
            Robot(
                robot_id="R1",
                current_position=Position(0, 0),
                target_position=Position(4, 4),
                state=RobotState.IDLE,
            )
        ]

        self.pathfinder = AStarPathfinder(self.warehouse_manager)
        self.calculate_routes()
        self.running = False

    def calculate_routes(self) -> None:
        """Calculate routes for robots that have targets."""

        for robot in self.robots:
            if robot.target_position is None:
                continue

            if robot.state in {
                RobotState.IDLE,
                RobotState.BLOCKED,
            }:
                robot.calculate_route(self.pathfinder)

    def step(self) -> None:
        """
        Advance the simulation by one movement step.

        Each robot moves at most one grid position.
        """

        for robot in self.robots:
            if robot.target_position is None:
                robot.state = RobotState.IDLE
                continue

            if robot.state == RobotState.COMPLETED:
                continue

            if robot.state == RobotState.BLOCKED:
                continue

            if not robot.route:
                robot.calculate_route(self.pathfinder)

            if robot.state == RobotState.BLOCKED:
                continue

            if not robot.route:
                robot.state = RobotState.WAITING
                continue

            next_position = (
                robot.route[1]
                if (
                    len(robot.route) > 1
                    and robot.route[0] == robot.current_position
                )
                else robot.route[0]
            )

            if not self.warehouse_manager.is_walkable(next_position):
                robot.block()
                continue

            robot.move_next()

    def add_shelf(self, shelf: Shelf) -> None:
        """Add a shelf to the simulation warehouse."""

        self.warehouse_manager.add_shelf(shelf)

    def add_robot(self, robot: Robot) -> None:
        """Add a robot to the simulation."""

        self.robots.append(robot)

    def get_robot(self, robot_id: str) -> Robot | None:
        """Return a robot by ID."""

        return next(
            (
                robot
                for robot in self.robots
                if robot.robot_id == robot_id
            ),
            None,
        )


def create_default_simulation() -> DigitalTwinSimulation:
    """Create the default five-by-five Digital Twin simulation."""

    warehouse = Warehouse(rows=5, columns=5)

    warehouse.add_shelf(
        Shelf(
            shelf_id="S1",
            position=Position(2, 2),
        )
    )

    robot = Robot(
        robot_id="R1",
        current_position=Position(0, 0),
        target_position=Position(4, 4),
        state=RobotState.IDLE,
    )

    simulation = DigitalTwinSimulation(
        warehouse=warehouse,
        robots=[robot],
    )

    simulation.calculate_routes()

    return simulation