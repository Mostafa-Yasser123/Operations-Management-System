from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# =========================
# Create
# =========================

class CustodyCreate(BaseModel):

    user_id: str = Field(
        ...,
        min_length=1
    )

    week_name: str = Field(
        ...,
        min_length=1
    )

    payment_date: date

    balance: Optional[Decimal] = None

    weekly_installment: Optional[Decimal] = None

    total_orders: Optional[int] = Field(
        None,
        ge=0
    )

    recorded_payment: Optional[Decimal] = None

    remaining_balance: Optional[Decimal] = None

    is_bonus: Optional[bool] = None


# =========================
# Update
# =========================

class CustodyUpdate(BaseModel):

    balance: Optional[Decimal] = None

    weekly_installment: Optional[Decimal] = None

    total_orders: Optional[int] = Field(
        None,
        ge=0
    )

    recorded_payment: Optional[Decimal] = None

    remaining_balance: Optional[Decimal] = None

    is_bonus: Optional[bool] = None


# =========================
# Response
# =========================

class CustodyResponse(BaseModel):

    user_id: str

    week_name: str

    payment_date: date

    balance: Optional[Decimal]

    weekly_installment: Optional[Decimal]

    total_orders: Optional[int]

    recorded_payment: Optional[Decimal]

    remaining_balance: Optional[Decimal]

    is_bonus: Optional[bool]

    created_at: Optional[datetime]

    class Config:
        from_attributes = True