"""
Pathfinding algorithms for the warehouse Digital Twin.

This module contains the A* shortest-path implementation.
It is independent of FastAPI, PostgreSQL, and frontend code.
"""

from __future__ import annotations

import heapq
from itertools import count

from simulation.models import Position
from simulation.warehouse import WarehouseManager


class AStarPathfinder:
    """Finds the shortest walkable path through a warehouse grid."""

    def __init__(self, warehouse: WarehouseManager) -> None:
        self._warehouse = warehouse

    @staticmethod
    def _heuristic(current: Position, goal: Position) -> int:
        """
        Calculate Manhattan distance between two positions.

        Since diagonal movement is not allowed, Manhattan distance
        is an admissible heuristic for this grid.
        """

        return abs(current.row - goal.row) + abs(current.column - goal.column)

    @staticmethod
    def _reconstruct_path(
        came_from: dict[Position, Position],
        current: Position,
    ) -> list[Position]:
        """Reconstruct the path from goal back to start."""

        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        path.reverse()
        return path

    def find_path(
        self,
        start: Position,
        goal: Position,
    ) -> list[Position] | None:
        """
        Find the shortest path from start to goal.

        Returns:
            A list of positions including start and goal,
            or None when no valid path exists.

        Raises:
            ValueError: If start or goal is outside the warehouse
                or either position is blocked.
        """

        if not self._warehouse.warehouse.is_valid_position(start):
            raise ValueError(f"Start position {start} is outside the warehouse.")

        if not self._warehouse.warehouse.is_valid_position(goal):
            raise ValueError(f"Goal position {goal} is outside the warehouse.")

        if not self._warehouse.is_walkable(start):
            raise ValueError(f"Start position {start} is blocked.")

        if not self._warehouse.is_walkable(goal):
            raise ValueError(f"Goal position {goal} is blocked.")

        if start == goal:
            return [start]

        sequence = count()

        open_set: list[tuple[int, int, Position]] = []

        heapq.heappush(
            open_set,
            (
                self._heuristic(start, goal),
                next(sequence),
                start,
            ),
        )

        came_from: dict[Position, Position] = {}

        g_score: dict[Position, int] = {
            start: 0,
        }

        while open_set:
            _, _, current = heapq.heappop(open_set)

            if current == goal:
                return self._reconstruct_path(came_from, current)

            current_cost = g_score[current]

            for neighbor in self._warehouse.get_neighbors(current):
                tentative_g_score = current_cost + 1

                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score

                    f_score = (
                        tentative_g_score
                        + self._heuristic(neighbor, goal)
                    )

                    heapq.heappush(
                        open_set,
                        (
                            f_score,
                            next(sequence),
                            neighbor,
                        ),
                    )

        return None