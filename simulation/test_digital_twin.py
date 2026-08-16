from simulation.digital_twin import DigitalTwinSimulation
from simulation.models import Position, Shelf, Warehouse
from simulation.robot import Robot, RobotState


def create_simulation() -> DigitalTwinSimulation:
    """Create a basic warehouse simulation for testing."""

    warehouse = Warehouse(5, 5)

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
    )

    return DigitalTwinSimulation(
        warehouse=warehouse,
        robots=[robot],
    )


def test_robot_moves_one_step():
    """Robot should move from its current position."""

    simulation = create_simulation()
    robot = simulation.robots[0]

    simulation.calculate_routes()

    assert robot.current_position == Position(0, 0)
    assert robot.state == RobotState.MOVING

    simulation.step()

    assert robot.current_position != Position(0, 0)
    assert robot.state == RobotState.MOVING


def test_robot_eventually_completes():
    """Robot should reach its target and become COMPLETED."""

    simulation = create_simulation()
    robot = simulation.robots[0]

    simulation.calculate_routes()

    for _ in range(30):
        simulation.step()

        if robot.state == RobotState.COMPLETED:
            break

    assert robot.current_position == Position(4, 4)
    assert robot.target_position == Position(4, 4)
    assert robot.state == RobotState.COMPLETED


def test_blocked_robot():
    """Robot should become BLOCKED when its target is blocked."""

    warehouse = Warehouse(5, 5)

    warehouse.add_shelf(
        Shelf(
            shelf_id="S1",
            position=Position(0, 1),
        )
    )

    robot = Robot(
        robot_id="R1",
        current_position=Position(0, 0),
        target_position=Position(0, 1),
    )

    simulation = DigitalTwinSimulation(
        warehouse=warehouse,
        robots=[robot],
    )

    simulation.calculate_routes()

    assert robot.state == RobotState.BLOCKED


def test_robot_without_target_stays_idle():
    """Robot without a target should remain IDLE."""

    warehouse = Warehouse(5, 5)

    robot = Robot(
        robot_id="R1",
        current_position=Position(0, 0),
    )

    simulation = DigitalTwinSimulation(
        warehouse=warehouse,
        robots=[robot],
    )

    simulation.step()

    assert robot.current_position == Position(0, 0)
    assert robot.state == RobotState.IDLE