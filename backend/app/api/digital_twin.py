"""
FastAPI endpoints for Digital Twin state.

This module exposes the current in-memory Digital Twin simulation state.
It does not contain simulation/pathfinding logic or database logic.
"""

from fastapi import APIRouter

from app.schemas.digital_twin import WarehouseStateResponse
from app.services.digital_twin import DigitalTwinStateService

from simulation.models import Position, Shelf, Warehouse
from simulation.robot import Robot, RobotState


router = APIRouter(
    prefix="/digital-twin",
    tags=["Digital Twin"],
)


# ---------------------------------------------------------------------------
# Simulation-only in-memory Digital Twin state
# ---------------------------------------------------------------------------

warehouse = Warehouse(rows=5, columns=5)

warehouse.add_shelf(
    Shelf(
        shelf_id="S1",
        position=Position(2, 2),
    )
)

robots = [
    Robot(
        robot_id="R1",
        current_position=Position(0, 0),
        target_position=Position(4, 4),
        state=RobotState.MOVING,
        route=[
            Position(0, 0),
            Position(0, 1),
            Position(1, 1),
            Position(4, 4),
        ],
    )
]


@router.get(
    "/state",
    response_model=WarehouseStateResponse,
)
def get_digital_twin_state() -> WarehouseStateResponse:
    """
    Return the current Digital Twin warehouse state.

    The state is currently maintained in memory for simulation purposes.
    No database or frontend integration is performed here.
    """

    return DigitalTwinStateService.warehouse_to_response(
        warehouse,
        robots,
    )