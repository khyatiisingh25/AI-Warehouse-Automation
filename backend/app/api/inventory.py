from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.inventory import (
    InventoryCreate,
    InventoryResponse,
    InventoryUpdate,
)
from app.services.inventory import (
    create_inventory,
    delete_inventory,
    get_inventories,
    get_inventory,
    update_inventory,
)


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"],
)


@router.post(
    "/",
    response_model=InventoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_inventory_endpoint(
    inventory_data: InventoryCreate,
    db: Session = Depends(get_db),
):
    return create_inventory(db, inventory_data)


@router.get(
    "/",
    response_model=list[InventoryResponse],
)
def get_inventory_list(
    db: Session = Depends(get_db),
):
    return get_inventories(db)


@router.get(
    "/{inventory_id}",
    response_model=InventoryResponse,
)
def get_inventory_endpoint(
    inventory_id: UUID,
    db: Session = Depends(get_db),
):
    inventory = get_inventory(db, inventory_id)

    if inventory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory not found",
        )

    return inventory


@router.put(
    "/{inventory_id}",
    response_model=InventoryResponse,
)
def update_inventory_endpoint(
    inventory_id: UUID,
    inventory_data: InventoryUpdate,
    db: Session = Depends(get_db),
):
    inventory = get_inventory(db, inventory_id)

    if inventory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory not found",
        )

    return update_inventory(db, inventory, inventory_data)


@router.delete(
    "/{inventory_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_inventory_endpoint(
    inventory_id: UUID,
    db: Session = Depends(get_db),
):
    inventory = get_inventory(db, inventory_id)

    if inventory is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Inventory not found",
        )

    delete_inventory(db, inventory)