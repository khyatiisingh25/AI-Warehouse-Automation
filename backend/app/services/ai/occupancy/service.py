from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ShelfOccupancyResult:
    shelf_id: str
    occupied: bool
    occupancy_ratio: float


class ShelfOccupancyService:
    """
    Estimate shelf occupancy from detected product bounding boxes.
    """

    def calculate(
        self,
        shelf_id: str,
        shelf_area: float,
        product_areas: list[float],
    ) -> ShelfOccupancyResult:
        if shelf_area <= 0:
            raise ValueError("Shelf area must be greater than zero.")

        occupied_area = sum(
            area for area in product_areas
            if area > 0
        )

        occupancy_ratio = min(
            occupied_area / shelf_area,
            1.0,
        )

        return ShelfOccupancyResult(
            shelf_id=shelf_id,
            occupied=occupancy_ratio > 0,
            occupancy_ratio=occupancy_ratio,
        )