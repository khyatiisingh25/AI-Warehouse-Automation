from simulation.models import Warehouse, Shelf, Position
from simulation.warehouse import WarehouseManager
from simulation.pathfinding import AStarPathfinder


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
