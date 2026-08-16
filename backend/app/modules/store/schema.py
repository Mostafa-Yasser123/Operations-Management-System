from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

from app.common.enums import StoreStatus


# =========================
# Create
# =========================

class StoreCreate(BaseModel):
    
    id: int = Field(
    ...,
    ge=0
    )
    
    item_name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    quantity: int = Field(
        ...,
        ge=0
    )

    unit_value: Decimal = Field(
        ...,
        ge=0
    )

    status: StoreStatus = StoreStatus.available


# =========================
# Update
# =========================

class StoreUpdate(BaseModel):

    item_name: Optional[str] = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    quantity: Optional[int] = Field(
        default=None,
        ge=0
    )

    unit_value: Optional[Decimal] = Field(
        default=None,
        ge=0
    )

    status: Optional[StoreStatus] = None

# =========================
# Response
# =========================

class StoreResponse(BaseModel):

    id: int

    item_name: str

    quantity: int

    unit_value: Decimal

    status: StoreStatus

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True