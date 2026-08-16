
from datetime import datetime

from sqlalchemy import (
    String,
    DateTime,
    ForeignKey,
    func,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    # =========================
    # Supervisor
    # =========================

    supervisor_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    # =========================
    # Delivery Rider
    # =========================

    delivery_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True,
        nullable=False
    )

    delivery_name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    # =========================
    # Created At
    # =========================

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )

    # =========================
    # Relationships
    # =========================

    supervisor = relationship(
        "User",
        foreign_keys=[supervisor_id]
    )

    delivery = relationship(
        "User",
        foreign_keys=[delivery_id]
    )

