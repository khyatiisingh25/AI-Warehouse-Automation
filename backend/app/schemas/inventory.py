from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class InventoryBase(BaseModel):
    product_id: UUID
    shelf_id: UUID
    quantity: int = Field(..., ge=0)
    minimum_stock: int = Field(default=10, ge=0)


class InventoryCreate(InventoryBase):
    pass


class InventoryUpdate(BaseModel):
    product_id: UUID | None = None
    shelf_id: UUID | None = None
    quantity: int | None = Field(default=None, ge=0)
    minimum_stock: int | None = Field(default=None, ge=0)


class InventoryResponse(InventoryBase):
    inventory_id: UUID
    last_updated: datetime

    model_config = ConfigDict(from_attributes=True)