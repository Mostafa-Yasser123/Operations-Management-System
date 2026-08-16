from datetime import datetime

from pydantic import BaseModel, Field


# =========================
# Create
# =========================

class AuditLogCreate(BaseModel):

    supervisor_id: str = Field(
        ...,
        min_length=1
    )

    delivery_id: str = Field(
        ...,
        min_length=1
    )

    delivery_name: str = Field(
        ...,
        min_length=1
    )


# =========================
# Update
# =========================

class AuditLogUpdate(BaseModel):

    supervisor_id: str = Field(
        ...,
        min_length=1
    )

    delivery_name: str = Field(
        ...,
        min_length=1
    )


# =========================
# Response
# =========================

class AuditLogResponse(BaseModel):

    supervisor_id: str

    delivery_id: str

    delivery_name: str

    created_at: datetime

    class Config:
        from_attributes = True

