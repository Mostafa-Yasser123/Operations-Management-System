
from datetime import datetime
from decimal import Decimal

from sqlalchemy import (
    Integer,
    ForeignKey,
    Numeric,
    DateTime,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


class Equipment(Base):

    __tablename__ = "equipment"

    # =========================
    # Composite Primary Key
    # =========================

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True,
        nullable=False
    )

    store_item_id: Mapped[int] = mapped_column(
        ForeignKey("store.id"),
        primary_key=True,
        nullable=False
    )

    # =========================
    # Equipment Data
    # =========================

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    unit_price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    total_value: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    issue_date: Mapped[datetime] = mapped_column(
        DateTime,
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
    # Relationships
    # =========================

    user = relationship("User")

    store_item = relationship("Store")

