from simulation.models import Warehouse, Shelf, Position
from simulation.warehouse import WarehouseManager
from simulation.pathfinding import AStarPathfinder
from simulation.robot import Robot


def test_path_avoids_shelf():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)

    manager.add_shelf(Shelf("S1", Position(2, 2)))

    pathfinder = AStarPathfinder(manager)
    path = pathfinder.find_path(Position(0, 0), Position(4, 4))

    assert path is not None
    assert Position(2, 2) not in path


def test_start_equals_goal():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)

    pathfinder = AStarPathfinder(manager)
    path = pathfinder.find_path(Position(1, 1), Position(1, 1))

    assert path == [Position(1, 1)]


def test_blocked_start_raises_error():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)

    manager.add_shelf(Shelf("S1", Position(0, 0)))

    pathfinder = AStarPathfinder(manager)

    try:
        pathfinder.find_path(Position(0, 0), Position(4, 4))
        assert False
    except ValueError:
        assert True

def test_blocked_goal_raises_error():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)

    manager.add_shelf(Shelf("S1", Position(4, 4)))

    pathfinder = AStarPathfinder(manager)

    try:
        pathfinder.find_path(Position(0, 0), Position(4, 4))
        assert False
    except ValueError:
        assert True

def test_invalid_start_raises_error():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)

    pathfinder = AStarPathfinder(manager)

    try:
        pathfinder.find_path(Position(-1, 0), Position(4, 4))
        assert False
    except ValueError:
        assert True 

def test_unreachable_destination_returns_none():
    warehouse = Warehouse(3, 3)
    manager = WarehouseManager(warehouse)

    manager.add_shelf(Shelf("S1", Position(0, 1)))
    manager.add_shelf(Shelf("S2", Position(1, 0)))
    manager.add_shelf(Shelf("S3", Position(1, 1)))
    manager.add_shelf(Shelf("S4", Position(1, 2)))
    manager.add_shelf(Shelf("S5", Position(2, 1)))

    pathfinder = AStarPathfinder(manager)

    path = pathfinder.find_path(
        Position(0, 0),
        Position(2, 2),
    )

    assert path is None       

def test_dynamic_obstacle_changes_path():
    warehouse = Warehouse(5, 5)
    manager = WarehouseManager(warehouse)

    pathfinder = AStarPathfinder(manager)

    # Initial path
    path_before = pathfinder.find_path(
        Position(0, 0),
        Position(4, 4),
    )

    assert path_before is not None

    # Add a shelf on the original route
    manager.add_shelf(
        Shelf("DYNAMIC-1", path_before[1])
    )

    # Calculate path again after warehouse state changed
    path_after = pathfinder.find_path(
        Position(0, 0),
        Position(4, 4),
    )

    assert path_after is not None
    assert path_before != path_after
    assert path_before[1] not in path_after    

def test_pathfinding_performance():
    warehouse = Warehouse(100, 100)
    manager = WarehouseManager(warehouse)

    pathfinder = AStarPathfinder(manager)

    import time

    start_time = time.perf_counter()

    path = pathfinder.find_path(
        Position(0, 0),
        Position(99, 99),
    )

    elapsed_time = time.perf_counter() - start_time

    assert path is not None

    print(f"\n100x100 pathfinding time: {elapsed_time:.6f} seconds")  

def test_robot_creation():
    robot = Robot("R1", Position(0, 0))

    assert robot.robot_id == "R1"
    assert robot.position == Position(0, 0)


def test_robot_position_update():
    robot = Robot("R1", Position(0, 0))

    robot.move_to(Position(2, 3))

    assert robot.position == Position(2, 3)      