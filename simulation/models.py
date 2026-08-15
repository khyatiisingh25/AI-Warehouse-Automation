"""
Core data models for the warehouse Digital Twin.

This module contains domain models only.
It does not depend on FastAPI, PostgreSQL, or frontend code.
"""

from dataclasses import dataclass, field


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
    """
    Represents a warehouse shelf in the Digital Twin.

    The first three fields preserve the existing simulation API:
        Shelf(shelf_id, position, products)

    Additional metadata fields support backend-aligned shelf
    information without requiring backend dependencies.
    """

    shelf_id: str
    position: Position
    products: list[Product] = field(default_factory=list)

    shelf_code: str = ""
    zone: str = ""
    rack: str = ""
    level: int = 0
    max_capacity: int = 0
    current_capacity: int = 0
    status: str = "Available"

    def __post_init__(self) -> None:
        if not self.shelf_id.strip():
            raise ValueError("shelf_id cannot be empty.")

        if self.shelf_code and not self.shelf_code.strip():
            raise ValueError("shelf_code cannot be empty.")

        if self.zone and not self.zone.strip():
            raise ValueError("zone cannot be empty.")

        if self.rack and not self.rack.strip():
            raise ValueError("rack cannot be empty.")

        if self.level < 0:
            raise ValueError("level cannot be negative.")

        if self.max_capacity < 0:
            raise ValueError("max_capacity cannot be negative.")

        if self.current_capacity < 0:
            raise ValueError("current_capacity cannot be negative.")

        if (
            self.max_capacity > 0
            and self.current_capacity > self.max_capacity
        ):
            raise ValueError(
                "current_capacity cannot exceed max_capacity."
            )

    @property
    def is_occupied(self) -> bool:
        """Return True when the shelf contains stored inventory."""

        return (
            self.current_capacity > 0
            or any(
                product.quantity > 0
                for product in self.products
            )
        )


@dataclass
class Warehouse:
    """Represents the logical state of a warehouse."""

    rows: int
    columns: int
    shelves: list[Shelf] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.rows <= 0:
            raise ValueError(
                "Warehouse rows must be greater than zero."
            )

        if self.columns <= 0:
            raise ValueError(
                "Warehouse columns must be greater than zero."
            )

    def is_valid_position(self, position: Position) -> bool:
        """Check whether a position lies inside the warehouse."""

        return (
            0 <= position.row < self.rows
            and 0 <= position.column < self.columns
        )

    def add_shelf(self, shelf: Shelf) -> None:
        """Add a shelf after validating its position."""

        if not self.is_valid_position(shelf.position):
            raise ValueError(
                f"Shelf position {shelf.position} is outside "
                "the warehouse."
            )

        if any(
            existing.shelf_id == shelf.shelf_id
            for existing in self.shelves
        ):
            raise ValueError(
                f"Shelf '{shelf.shelf_id}' already exists."
            )

        self.shelves.append(shelf)

    def is_blocked(self, position: Position) -> bool:
        """Return True if a shelf occupies the given position."""

        return any(
            shelf.position == position
            for shelf in self.shelves
        )