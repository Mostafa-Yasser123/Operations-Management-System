from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# =========================
# Create
# =========================

class EquipmentCreate(BaseModel):

    user_id: str = Field(
        ...,
        min_length=1
    )

    store_item_id: int = Field(
        ...,
        gt=0
    )

    quantity: int = Field(
        ...,
        gt=0
    )

    issue_date: datetime


# =========================
# Update
# =========================

class EquipmentUpdate(BaseModel):

    quantity: Optional[int] = Field(
        None,
        gt=0
    )

    issue_date: Optional[datetime] = None


# =========================
# Response
# =========================

class EquipmentResponse(BaseModel):

    user_id: str

    store_item_id: int

    quantity: int

    unit_price: Decimal

    total_value: Decimal

    issue_date: datetime

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True