from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def create_product(db: Session, product_data: ProductCreate) -> Product:
    product = Product(**product_data.model_dump())

    db.add(product)
    db.commit()
    db.refresh(product)

    return product


def get_product(db: Session, product_id: UUID) -> Product | None:
    statement = select(Product).where(Product.product_id == product_id)

    return db.scalar(statement)


def get_products(db: Session) -> list[Product]:
    statement = select(Product).order_by(Product.created_at.desc())

    return list(db.scalars(statement).all())


def update_product(
    db: Session,
    product: Product,
    product_data: ProductUpdate,
) -> Product:
    update_data = product_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(product, field, value)

    db.commit()
    db.refresh(product)

    return product


def delete_product(db: Session, product: Product) -> None:
    db.delete(product)
    db.commit()