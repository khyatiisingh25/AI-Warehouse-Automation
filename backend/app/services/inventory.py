from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.schemas.inventory import InventoryCreate, InventoryUpdate


def create_inventory(
    db: Session,
    inventory_data: InventoryCreate,
) -> Inventory:
    inventory = Inventory(**inventory_data.model_dump())

    db.add(inventory)
    db.commit()
    db.refresh(inventory)

    return inventory


def get_inventory(
    db: Session,
    inventory_id: UUID,
) -> Inventory | None:
    statement = select(Inventory).where(
        Inventory.inventory_id == inventory_id
    )

    return db.scalar(statement)


def get_inventories(db: Session) -> list[Inventory]:
    statement = select(Inventory).order_by(
        Inventory.last_updated.desc()
    )

    return list(db.scalars(statement).all())


def update_inventory(
    db: Session,
    inventory: Inventory,
    inventory_data: InventoryUpdate,
) -> Inventory:
    update_data = inventory_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(inventory, field, value)

    db.commit()
    db.refresh(inventory)

    return inventory


def delete_inventory(
    db: Session,
    inventory: Inventory,
) -> None:
    db.delete(inventory)
    db.commit()