"""
FastAPI endpoints for Digital Twin state and simulation control.
"""

from fastapi import APIRouter, HTTPException

from app.schemas.digital_twin import WarehouseStateResponse
from app.services.digital_twin import DigitalTwinStateService

from simulation.digital_twin import create_default_simulation


router = APIRouter(
    prefix="/digital-twin",
    tags=["Digital Twin"],
)


# Live in-memory Digital Twin simulation.
simulation = create_default_simulation()


def _get_state() -> WarehouseStateResponse:
    """Convert the current simulation state into an API response."""

    return DigitalTwinStateService.warehouse_to_response(
        simulation.warehouse,
        simulation.robots,
        running=simulation.running,
    )


@router.get(
    "/state",
    response_model=WarehouseStateResponse,
)
def get_digital_twin_state() -> WarehouseStateResponse:
    """Return the latest Digital Twin simulation state."""

    return _get_state()


@router.post(
    "/start",
    response_model=WarehouseStateResponse,
)
def start_digital_twin() -> WarehouseStateResponse:
    """Start the Digital Twin simulation."""

    try:
        simulation.start()
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=409,
            detail=f"Unable to start Digital Twin simulation: {exc}",
        ) from exc

    return _get_state()


@router.post(
    "/step",
    response_model=WarehouseStateResponse,
)
def advance_digital_twin() -> WarehouseStateResponse:
    """Advance the Digital Twin simulation by one movement step."""

    if not simulation.running:
        raise HTTPException(
            status_code=409,
            detail="Digital Twin simulation is not running.",
        )

    try:
        simulation.step()
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=409,
            detail=f"Unable to advance Digital Twin simulation: {exc}",
        ) from exc

    return _get_state()


@router.post(
    "/reset",
    response_model=WarehouseStateResponse,
)
def reset_digital_twin() -> WarehouseStateResponse:
    """Reset the Digital Twin simulation to its initial state."""

    try:
        simulation.reset()
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(
            status_code=409,
            detail=f"Unable to reset Digital Twin simulation: {exc}",
        ) from exc

    return _get_state()