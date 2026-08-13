from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Shelf(Base):
    __tablename__ = "shelves"

    shelf_id: Mapped[UUID] = mapped_column(
        primary_key=True,
        default=uuid4,
    )

    shelf_code: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        index=True,
        nullable=False,
    )

    zone: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    rack: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    level: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    max_capacity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    current_capacity: Mapped[int] = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="Available",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False,
    )