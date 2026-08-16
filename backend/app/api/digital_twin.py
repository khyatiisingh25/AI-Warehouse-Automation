"""
FastAPI endpoints for Digital Twin state and simulation control.
"""

from fastapi import APIRouter

from app.schemas.digital_twin import WarehouseStateResponse
from app.services.digital_twin import DigitalTwinStateService

from simulation.digital_twin import create_default_simulation


router = APIRouter(
    prefix="/digital-twin",
    tags=["Digital Twin"],
)


# Live in-memory Digital Twin simulation.
simulation = create_default_simulation()


@router.get(
    "/state",
    response_model=WarehouseStateResponse,
)
def get_digital_twin_state() -> WarehouseStateResponse:
    """Return the latest Digital Twin simulation state."""

    return DigitalTwinStateService.warehouse_to_response(
        simulation.warehouse,
        simulation.robots,
    )


@router.post(
    "/step",
    response_model=WarehouseStateResponse,
)
def advance_digital_twin() -> WarehouseStateResponse:
    """Advance the Digital Twin simulation by one movement step."""

    simulation.step()

    return DigitalTwinStateService.warehouse_to_response(
        simulation.warehouse,
        simulation.robots,
    )