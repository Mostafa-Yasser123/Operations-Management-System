from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field

from app.common.enums import UserRole
from app.common.enums import VehicleType

class UserCreate(BaseModel):
    id: str = Field(..., description="User ID")

    name: str = Field(..., min_length=3, max_length=100)

    user_name: str = Field(..., min_length=3, max_length=50)

    password: str = Field(..., min_length=6)

    phone_number: str = Field(
        ...,
        pattern=r"^01[0125]\d{8}$",
        description="Egyptian mobile number"
    )

    talabat_e_mail: EmailStr

    role: UserRole

    sp: str

    first_contract_date: datetime

    year: Optional[int] = None

    zone: str | None = None
    city: str | None = None
    alt_phone_number: str | None = None
    relation: str | None = None
    national_id_no: str | None = None
    vehicle: VehicleType | None = None
    education: str | None = None
    bike_number: str | None = None
    last_shift_date: datetime | None = None


class UserResponse(BaseModel):
    id: str
    name: str
    user_name: str
    phone_number: str
    talabat_e_mail: EmailStr
    role: UserRole

    sp: str
    first_contract_date: datetime

    year: int | None = None

    zone: str | None = None
    city: str | None = None
    alt_phone_number: str | None = None
    relation: str | None = None
    national_id_no: str | None = None
    vehicle: VehicleType | None = None
    education: str | None = None
    bike_number: str | None = None
    last_shift_date: datetime | None = None
    termination_reason: str | None = None

    is_active: bool
    is_available: bool
    is_termination: bool

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserTermination(BaseModel):
    last_shift_date: datetime
    termination_reason: str = Field(
        ...,
        min_length=3,
        max_length=255
    )

class UserUpdate(BaseModel):

    name: Optional[str] = Field(None, min_length=3, max_length=100)

    phone_number: Optional[str] = Field(
        None,
        pattern=r"^01[0125]\d{8}$"
    )

    talabat_e_mail: Optional[EmailStr] = None

    role: Optional[UserRole] = None

    sp: Optional[str] = None

    first_contract_date: Optional[datetime] = None

    year: Optional[int] = None

    zone: Optional[str] = None
    city: Optional[str] = None
    alt_phone_number: Optional[str] = None
    relation: Optional[str] = None
    national_id_no: Optional[str] = None

    vehicle: Optional[VehicleType] = None

    education: Optional[str] = None

    bike_number: Optional[str] = None

    last_shift_date: Optional[datetime] = None            