"""
Warehouse operations for the Digital Twin.

This module provides higher-level operations on the warehouse model,
including walkability checks, blocked positions, and grid generation.
"""

from __future__ import annotations

from simulation.models import Position, Shelf, Warehouse


class WarehouseManager:
    """Provides operational access to a warehouse simulation."""

    def __init__(self, warehouse: Warehouse) -> None:
        self._warehouse = warehouse

    @property
    def warehouse(self) -> Warehouse:
        """Return the underlying warehouse model."""

        return self._warehouse

    def add_shelf(self, shelf: Shelf) -> None:
        """Add a shelf to the warehouse."""

        self._warehouse.add_shelf(shelf)

    def is_walkable(self, position: Position) -> bool:
        """Return True if a position is inside the warehouse and unblocked."""

        return (
            self._warehouse.is_valid_position(position)
            and not self._warehouse.is_blocked(position)
        )

    def get_blocked_positions(self) -> set[Position]:
        """Return all positions currently occupied by shelves."""

        return {
            shelf.position
            for shelf in self._warehouse.shelves
        }

    def get_walkable_positions(self) -> set[Position]:
        """Return all currently walkable positions."""

        return {
            Position(row, column)
            for row in range(self._warehouse.rows)
            for column in range(self._warehouse.columns)
            if self.is_walkable(Position(row, column))
        }

    def get_neighbors(self, position: Position) -> list[Position]:
        """
        Return valid four-directional neighboring positions.

        Diagonal movement is intentionally excluded because warehouse
        picking routes normally operate along aisles.
        """

        candidates = [
            Position(position.row - 1, position.column)
            if position.row > 0
            else None,

            Position(position.row + 1, position.column)
            if position.row < self._warehouse.rows - 1
            else None,

            Position(position.row, position.column - 1)
            if position.column > 0
            else None,

            Position(position.row, position.column + 1)
            if position.column < self._warehouse.columns - 1
            else None,
        ]

        return [
            candidate
            for candidate in candidates
            if candidate is not None and self.is_walkable(candidate)
        ]

    def to_grid(self) -> list[list[int]]:
        """
        Convert the warehouse into a simple pathfinding grid.

        0 = walkable
        1 = blocked
        """

        return [
            [
                1
                if self._warehouse.is_blocked(Position(row, column))
                else 0
                for column in range(self._warehouse.columns)
            ]
            for row in range(self._warehouse.rows)
        ]