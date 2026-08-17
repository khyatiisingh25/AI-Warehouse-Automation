from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class ShelfBase(BaseModel):
    shelf_code: str = Field(..., max_length=50)
    zone: str = Field(..., max_length=50)
    rack: str = Field(..., max_length=50)
    level: int = Field(..., ge=1)
    max_capacity: int = Field(..., ge=0)
    current_capacity: int = Field(default=0, ge=0)
    status: str = Field(default="Available", max_length=20)


class ShelfCreate(ShelfBase):
    pass


class ShelfUpdate(BaseModel):
    shelf_code: str | None = Field(default=None, max_length=50)
    zone: str | None = Field(default=None, max_length=50)
    rack: str | None = Field(default=None, max_length=50)
    level: int | None = Field(default=None, ge=1)
    max_capacity: int | None = Field(default=None, ge=0)
    current_capacity: int | None = Field(default=None, ge=0)
    status: str | None = Field(default=None, max_length=20)


class ShelfResponse(ShelfBase):
    shelf_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)