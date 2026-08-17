from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.shelf import ShelfCreate, ShelfResponse, ShelfUpdate
from app.services.shelf import (
    create_shelf,
    delete_shelf,
    get_shelf,
    get_shelves,
    update_shelf,
)


router = APIRouter(
    prefix="/shelves",
    tags=["Shelves"],
)


@router.post(
    "/",
    response_model=ShelfResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_shelf_endpoint(
    shelf_data: ShelfCreate,
    db: Session = Depends(get_db),
):
    return create_shelf(db, shelf_data)


@router.get(
    "/",
    response_model=list[ShelfResponse],
)
def get_shelf_list(
    db: Session = Depends(get_db),
):
    return get_shelves(db)


@router.get(
    "/{shelf_id}",
    response_model=ShelfResponse,
)
def get_shelf_endpoint(
    shelf_id: UUID,
    db: Session = Depends(get_db),
):
    shelf = get_shelf(db, shelf_id)

    if shelf is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shelf not found",
        )

    return shelf


@router.put(
    "/{shelf_id}",
    response_model=ShelfResponse,
)
def update_shelf_endpoint(
    shelf_id: UUID,
    shelf_data: ShelfUpdate,
    db: Session = Depends(get_db),
):
    shelf = get_shelf(db, shelf_id)

    if shelf is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shelf not found",
        )

    return update_shelf(db, shelf, shelf_data)


@router.delete(
    "/{shelf_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_shelf_endpoint(
    shelf_id: UUID,
    db: Session = Depends(get_db),
):
    shelf = get_shelf(db, shelf_id)

    if shelf is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Shelf not found",
        )

    delete_shelf(db, shelf)