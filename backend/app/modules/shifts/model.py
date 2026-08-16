from datetime import date, datetime
from sqlalchemy import (
    String,
    Date,
    Time,
    DateTime,
    ForeignKey,
    PrimaryKeyConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Shift(Base):

    __tablename__ = "shifts"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    shift_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    start_time: Mapped[datetime] = mapped_column(
        Time,
        nullable=False
    )

    end_time: Mapped[datetime] = mapped_column(
        Time,
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

    __table_args__ = (
        PrimaryKeyConstraint(
            "user_id",
            "shift_date",
            name="pk_shifts"
        ),
    )