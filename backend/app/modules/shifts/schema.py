from datetime import date, time, datetime
from typing import Optional

from pydantic import BaseModel, Field


# =========================
# Create
# =========================

class ShiftCreate(BaseModel):

    user_id: str = Field(
        ...,
        min_length=1
    )

    shift_date: date

    start_time: time

    end_time: time


# =========================
# Update
# =========================

class ShiftUpdate(BaseModel):

    start_time: Optional[time] = None

    end_time: Optional[time] = None


# =========================
# Response
# =========================

class ShiftResponse(BaseModel):

    user_id: str

    shift_date: date

    start_time: time

    end_time: time

    created_at: datetime

    updated_at: datetime

    class Config:
        from_attributes = True