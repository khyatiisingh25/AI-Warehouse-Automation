from app.services.ai.occupancy.service import ShelfOccupancyService


def test_shelf_occupancy():
    service = ShelfOccupancyService()

    result = service.calculate(
        shelf_id="SHELF-01",
        shelf_area=1000,
        product_areas=[200, 150, 100],
    )

    assert result.shelf_id == "SHELF-01"
    assert result.occupied is True
    assert result.occupancy_ratio == 0.45


def test_empty_shelf():
    service = ShelfOccupancyService()

    result = service.calculate(
        shelf_id="SHELF-02",
        shelf_area=1000,
        product_areas=[],
    )

    assert result.occupied is False
    assert result.occupancy_ratio == 0.0


def test_occupancy_cannot_exceed_100_percent():
    service = ShelfOccupancyService()

    result = service.calculate(
        shelf_id="SHELF-03",
        shelf_area=100,
        product_areas=[80, 80],
    )

    assert result.occupancy_ratio == 1.0
