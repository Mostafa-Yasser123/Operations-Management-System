from sqlalchemy import (
    String,
    Integer,
    Numeric,
    DateTime,
    Enum,
    func,
)

from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.common.enums import StoreStatus


class Store(Base):
    __tablename__ = "store"

    id: Mapped[int] = mapped_column(
         Integer,
        primary_key=True,
        autoincrement= False
    )

    item_name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    unit_value: Mapped[float] = mapped_column(
        Numeric(10, 2),
        nullable=False,
        default=0
    )

    status: Mapped[StoreStatus] = mapped_column(
        Enum(StoreStatus),
        nullable=False,
        default=StoreStatus.available
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )