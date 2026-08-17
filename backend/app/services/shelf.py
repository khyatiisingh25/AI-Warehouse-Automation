from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.shelf import Shelf
from app.schemas.shelf import ShelfCreate, ShelfUpdate


def create_shelf(
    db: Session,
    shelf_data: ShelfCreate,
) -> Shelf:
    shelf = Shelf(**shelf_data.model_dump())

    db.add(shelf)
    db.commit()
    db.refresh(shelf)

    return shelf


def get_shelf(
    db: Session,
    shelf_id: UUID,
) -> Shelf | None:
    statement = select(Shelf).where(
        Shelf.shelf_id == shelf_id
    )

    return db.scalar(statement)


def get_shelves(db: Session) -> list[Shelf]:
    statement = select(Shelf).order_by(
        Shelf.created_at.desc()
    )

    return list(db.scalars(statement).all())


def update_shelf(
    db: Session,
    shelf: Shelf,
    shelf_data: ShelfUpdate,
) -> Shelf:
    update_data = shelf_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(shelf, field, value)

    db.commit()
    db.refresh(shelf)

    return shelf


def delete_shelf(
    db: Session,
    shelf: Shelf,
) -> None:
    db.delete(shelf)
    db.commit()