from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# =========================
# Create
# =========================

class PerformanceCreate(BaseModel):

    user_id: str = Field(
        ...,
        min_length=1
    )

    log_date: date

    orders: int = Field(
        ...,
        ge=0
    )

    hours: Decimal = Field(
        ...,
        ge=0
    )

    acceptance_rate: Decimal = Field(
        ...,
        ge=0,
        le=100
    )

# =========================
# Update
# =========================

class PerformanceUpdate(BaseModel):

    orders: Optional[int] = Field(
        None,
        ge=0
    )

    hours: Optional[Decimal] = Field(
        None,
        ge=0
    )

    acceptance_rate: Optional[Decimal] = Field(
        None,
        ge=0,
        le=100
    )


# =========================
# Response
# =========================

class PerformanceResponse(BaseModel):

    user_id: str

    log_date: date

    orders: Optional[int] = None

    hours: Optional[Decimal] = None

    acceptance_rate: Optional[Decimal] = None

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True