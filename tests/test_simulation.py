"""Tests for the warehouse Digital Twin and pathfinding components."""

import pytest

from simulation.models import Position, Product, Shelf, Warehouse
from simulation.pathfinding import AStarPathfinder
from simulation.warehouse import WarehouseManager


def create_warehouse_manager(rows: int = 5, columns: int = 5) -> WarehouseManager:
    """Create a warehouse manager for testing."""

    return WarehouseManager(Warehouse(rows, columns))


def test_position_rejects_negative_coordinates() -> None:
    """Negative warehouse coordinates should be rejected."""

    with pytest.raises(ValueError):
        Position(-1, 0)


def test_product_rejects_negative_quantity() -> None:
    """Product quantity cannot be negative."""

    with pytest.raises(ValueError):
        Product("P1", "Keyboard", -1)


def test_shelf_is_occupied_when_product_has_quantity() -> None:
    """A shelf with available product should be marked occupied."""

    shelf = Shelf(
        "S1",
        Position(1, 1),
        [Product("P1", "Keyboard", 10)],
    )

    assert shelf.is_occupied is True


def test_shelf_is_not_occupied_when_quantity_is_zero() -> None:
    """A shelf with zero product quantity should not be occupied."""

    shelf = Shelf(
        "S1",
        Position(1, 1),
        [Product("P1", "Keyboard", 0)],
    )

    assert shelf.is_occupied is False


def test_warehouse_rejects_invalid_dimensions() -> None:
    """Warehouse dimensions must be positive."""

    with pytest.raises(ValueError):
        Warehouse(0, 5)


def test_shelf_can_be_added_to_warehouse() -> None:
    """A valid shelf should be added successfully."""

    manager = create_warehouse_manager()

    manager.add_shelf(
        Shelf("S1", Position(2, 2))
    )

    assert Position(2, 2) in manager.get_blocked_positions()


def test_warehouse_grid_marks_shelf_as_blocked() -> None:
    """Shelf positions should appear as blocked cells."""

    manager = create_warehouse_manager()

    manager.add_shelf(
        Shelf("S1", Position(2, 2))
    )

    grid = manager.to_grid()

    assert grid[2][2] == 1
    assert grid[0][0] == 0


def test_neighbors_do_not_include_blocked_positions() -> None:
    """Blocked cells should not be returned as neighbors."""

    manager = create_warehouse_manager()

    manager.add_shelf(
        Shelf("S1", Position(1, 2))
    )

    neighbors = manager.get_neighbors(Position(1, 1))

    assert Position(1, 2) not in neighbors


def test_astar_finds_shortest_path() -> None:
    """A* should find the shortest path around an obstacle."""

    manager = create_warehouse_manager()

    manager.add_shelf(
        Shelf("S1", Position(2, 2))
    )

    pathfinder = AStarPathfinder(manager)

    path = pathfinder.find_path(
        Position(0, 0),
        Position(4, 4),
    )

    assert path is not None
    assert path[0] == Position(0, 0)
    assert path[-1] == Position(4, 4)
    assert len(path) - 1 == 8


def test_astar_rejects_blocked_start() -> None:
    """A* should reject a blocked starting position."""

    manager = create_warehouse_manager()

    manager.add_shelf(
        Shelf("S1", Position(0, 0))
    )

    pathfinder = AStarPathfinder(manager)

    with pytest.raises(ValueError, match="Start position"):
        pathfinder.find_path(
            Position(0, 0),
            Position(4, 4),
        )


def test_astar_rejects_blocked_goal() -> None:
    """A* should reject a blocked destination."""

    manager = create_warehouse_manager()

    manager.add_shelf(
        Shelf("S1", Position(4, 4))
    )

    pathfinder = AStarPathfinder(manager)

    with pytest.raises(ValueError, match="Goal position"):
        pathfinder.find_path(
            Position(0, 0),
            Position(4, 4),
        )


def test_astar_returns_none_when_no_path_exists() -> None:
    """A* should return None when the destination is unreachable."""

    manager = create_warehouse_manager(3, 3)

    blocked_positions = [
        Position(0, 1),
        Position(1, 0),
        Position(1, 2),
        Position(2, 1),
    ]

    for index, position in enumerate(blocked_positions):
        manager.add_shelf(
            Shelf(f"S{index}", position)
        )

    pathfinder = AStarPathfinder(manager)

    path = pathfinder.find_path(
        Position(0, 0),
        Position(2, 2),
    )

    assert path is None