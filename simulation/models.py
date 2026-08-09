"""
Core data models for the warehouse Digital Twin.

This module contains domain models only.
It does not depend on FastAPI, PostgreSQL, or frontend code.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class Position:
    """Represents a coordinate in the warehouse grid."""

    row: int
    column: int

    def __post_init__(self) -> None:
        if self.row < 0 or self.column < 0:
            raise ValueError("Warehouse coordinates cannot be negative.")


@dataclass
class Product:
    """Represents a product stored in the warehouse."""

    product_id: str
    name: str
    quantity: int = 0

    def __post_init__(self) -> None:
        if not self.product_id.strip():
            raise ValueError("product_id cannot be empty.")

        if not self.name.strip():
            raise ValueError("Product name cannot be empty.")

        if self.quantity < 0:
            raise ValueError("Product quantity cannot be negative.")


@dataclass
class Shelf:
    """Represents a warehouse shelf and its stored products."""

    shelf_id: str
    position: Position
    products: list[Product] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not self.shelf_id.strip():
            raise ValueError("shelf_id cannot be empty.")

    @property
    def is_occupied(self) -> bool:
        """Return True when the shelf contains at least one product."""

        return any(product.quantity > 0 for product in self.products)


@dataclass
class Warehouse:
    """Represents the logical state of a warehouse."""

    rows: int
    columns: int
    shelves: list[Shelf] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.rows <= 0:
            raise ValueError("Warehouse rows must be greater than zero.")

        if self.columns <= 0:
            raise ValueError("Warehouse columns must be greater than zero.")

    def is_valid_position(self, position: Position) -> bool:
        """Check whether a position lies inside the warehouse."""

        return (
            0 <= position.row < self.rows
            and 0 <= position.column < self.columns
        )

    def add_shelf(self, shelf: Shelf) -> None:
        """Add a shelf to the warehouse after validating its position."""

        if not self.is_valid_position(shelf.position):
            raise ValueError(
                f"Shelf position {shelf.position} is outside the warehouse."
            )

        if any(existing.shelf_id == shelf.shelf_id for existing in self.shelves):
            raise ValueError(f"Shelf '{shelf.shelf_id}' already exists.")

        self.shelves.append(shelf)

    def is_blocked(self, position: Position) -> bool:
        """Return True if a shelf occupies the given position."""

        return any(
            shelf.position == position
            for shelf in self.shelves
        )