from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )

    product_id: Mapped[UUID] = mapped_column(
        ForeignKey("products.product_id"),
        nullable=False,
        index=True,
    )

    shelf_id: Mapped[UUID] = mapped_column(
        ForeignKey("shelves.shelf_id"),
        nullable=False,
        index=True,
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    minimum_stock: Mapped[int] = mapped_column(
        Integer,
        default=10,
        nullable=False,
    )

    last_updated: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )