from datetime import datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    sku: str = Field(..., max_length=50)
    product_name: str = Field(..., max_length=255)
    category: str = Field(..., max_length=100)
    brand: str | None = Field(default=None, max_length=100)
    description: str | None = None
    unit_price: Decimal = Field(..., ge=0, decimal_places=2)
    weight: Decimal | None = Field(default=None, ge=0, decimal_places=2)
    barcode: str | None = Field(default=None, max_length=100)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    sku: str | None = Field(default=None, max_length=50)
    product_name: str | None = Field(default=None, max_length=255)
    category: str | None = Field(default=None, max_length=100)
    brand: str | None = Field(default=None, max_length=100)
    description: str | None = None
    unit_price: Decimal | None = Field(default=None, ge=0, decimal_places=2)
    weight: Decimal | None = Field(default=None, ge=0, decimal_places=2)
    barcode: str | None = Field(default=None, max_length=100)


class ProductResponse(ProductBase):
    product_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)