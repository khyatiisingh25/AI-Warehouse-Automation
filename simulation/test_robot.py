from simulation.models import Position, Warehouse, Shelf
from simulation.pathfinding import AStarPathfinder
from simulation.robot import Robot, RobotState
from simulation.warehouse import WarehouseManager


def test_robot_initial_state():
    robot = Robot("R1", Position(0, 0))

    assert robot.robot_id == "R1"
    assert robot.position == Position(0, 0)
    assert robot.current_position == Position(0, 0)
    assert robot.target_position is None
    assert robot.route == []
    assert robot.state == RobotState.IDLE


def test_robot_set_target():
    robot = Robot("R1", Position(0, 0))

    robot.set_target(Position(4, 4))

    assert robot.target_position == Position(4, 4)
    assert robot.route == []
    assert robot.state == RobotState.IDLE


def test_robot_calculates_route_using_astar():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)
    pathfinder = AStarPathfinder(manager)

    robot = Robot("R1", Position(0, 0))
    robot.set_target(Position(4, 4))

    route = robot.calculate_route(pathfinder)

    assert route is not None
    assert len(route) > 0
    assert route[0] == Position(0, 0)
    assert route[-1] == Position(4, 4)
    assert robot.route == route
    assert robot.state == RobotState.MOVING


def test_robot_moves_along_route():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)
    pathfinder = AStarPathfinder(manager)

    robot = Robot("R1", Position(0, 0))
    robot.set_target(Position(2, 2))

    robot.calculate_route(pathfinder)

    initial_position = robot.current_position

    moved = robot.move_next()

    assert moved is True
    assert robot.current_position != initial_position
    assert robot.state in (
        RobotState.MOVING,
        RobotState.COMPLETED,
    )


def test_robot_reaches_target():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)
    pathfinder = AStarPathfinder(manager)

    robot = Robot("R1", Position(0, 0))
    robot.set_target(Position(2, 2))

    robot.calculate_route(pathfinder)

    while robot.state != RobotState.COMPLETED:
        moved = robot.move_next()

        if not moved:
            break

    assert robot.current_position == Position(2, 2)
    assert robot.state == RobotState.COMPLETED


def test_robot_becomes_blocked_when_target_is_blocked():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)

    manager.add_shelf(
        Shelf(
            "S1",
            Position(4, 4),
        )
    )

    pathfinder = AStarPathfinder(manager)

    robot = Robot("R1", Position(0, 0))
    robot.set_target(Position(4, 4))

    route = robot.calculate_route(pathfinder)

    assert route is None
    assert robot.route == []
    assert robot.state == RobotState.BLOCKED


def test_robot_move_to_keeps_compatibility():
    robot = Robot("R1", Position(0, 0))

    robot.move_to(Position(2, 3))

    assert robot.position == Position(2, 3)
    assert robot.current_position == Position(2, 3)


def test_robot_block_state():
    robot = Robot("R1", Position(0, 0))

    robot.block()

    assert robot.state == RobotState.BLOCKED


def test_robot_wait_state():
    robot = Robot("R1", Position(0, 0))

    robot.wait()

    assert robot.state == RobotState.WAITING


def test_robot_reset():
    robot = Robot("R1", Position(0, 0))

    robot.set_target(Position(4, 4))
    robot.route = [Position(0, 0), Position(1, 0)]
    robot.state = RobotState.MOVING

    robot.reset()

    assert robot.target_position is None
    assert robot.route == []
    assert robot.state == RobotState.IDLE