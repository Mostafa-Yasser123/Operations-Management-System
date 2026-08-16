from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class MasterPerformance(Base):

    __tablename__ = "master_performance"

    # =========================
    # Rider
    # =========================

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    # =========================
    # Performance Date
    # =========================

    log_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    # =========================
    # Orders
    # =========================

    orders: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    # =========================
    # Hours
    # =========================

    hours: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    # =========================
    # Acceptance Rate
    # =========================

    acceptance_rate: Mapped[Decimal] = mapped_column(
        Numeric(5, 2),
        nullable=False
    )

    # =========================
    # Timestamps
    # =========================

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

    # =========================
    # Composite Primary Key
    # =========================

    __table_args__ = (
        PrimaryKeyConstraint(
            "user_id",
            "log_date",
            name="pk_master_performance"
        ),
    )