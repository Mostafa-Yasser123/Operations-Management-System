from datetime import datetime

from sqlalchemy import String, Boolean, Integer, DateTime, Enum, func
from sqlalchemy.orm import Mapped, mapped_column

from app.common.enums import UserRole, VehicleType
from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    phone_number: Mapped[str] = mapped_column(String, nullable=False)

    sp: Mapped[str] = mapped_column(String, nullable=False)

    zone: Mapped[str] = mapped_column(String, nullable=False)

    city: Mapped[str] = mapped_column(String, nullable=False)

    alt_phone_number: Mapped[str] = mapped_column(String, nullable=False)

    relation: Mapped[str] = mapped_column(String, nullable=False)

    national_id_no: Mapped[str] = mapped_column(String, nullable=False)

    talabat_e_mail: Mapped[str] = mapped_column(String, nullable=False)

    vehicle: Mapped[VehicleType | None] = mapped_column(
        Enum(
            VehicleType,
            name="vehicle_type",
            values_callable=lambda enum: [e.value for e in enum]
        ),
        nullable=True
    )

    education: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    first_contract_date: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    last_shift_date: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    role: Mapped[UserRole] = mapped_column(
        Enum(
            UserRole,
            name="user_role",
            values_callable=lambda enum: [e.value for e in enum]
        ),
        nullable=False
    )

    user_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    hash_password: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    bike_number: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    termination_reason: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    is_termination: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    is_available: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now()
    )