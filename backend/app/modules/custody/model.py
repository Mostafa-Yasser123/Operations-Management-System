from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    String,
    func,
)

from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Custody(Base):

    __tablename__ = "custody"

    # =========================
    # User
    # =========================

    user_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("users.id"),
        nullable=False
    )

    # =========================
    # Week
    # =========================

    week_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    # =========================
    # Payment Date
    # =========================

    payment_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    # =========================
    # Custody Details
    # =========================

    balance: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    weekly_installment: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    total_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    recorded_payment: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    remaining_balance: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    is_bonus: Mapped[bool | None] = mapped_column(
        Boolean,
        nullable=True
    )

    # =========================
    # Created At
    # =========================

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=func.now()
    )

    # =========================
    # Composite Primary Key
    # =========================

    __table_args__ = (
        PrimaryKeyConstraint(
            "user_id",
            "week_name",
            "payment_date",
            name="pk_custody"
        ),
    )