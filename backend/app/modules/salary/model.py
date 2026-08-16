from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Integer,
    Numeric,
    SmallInteger,
    Text,
    String,
    PrimaryKeyConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class SalaryDetail(Base):

    __tablename__ = "salary_details"

    # =========================
    # User
    # =========================

    user_id: Mapped[str] = mapped_column(
        String,
        ForeignKey("users.id"),
        nullable=False
    )

    # =========================
    # Payroll
    # =========================

    payroll_year: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    payroll_month: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    payroll_week: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    week_label: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    # =========================
    # Rider Information
    # =========================

    rider_name: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    vehicle_type: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    smart_wallet: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    account_type: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    # =========================
    # Orders
    # =========================

    total_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    completed_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    pickup_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    delivery_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    cancelled_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    refunded_cancelled_orders: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    tmart_completed_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    tmart_pickup_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    tmart_delivery_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    tmart_cancelled_orders: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    # =========================
    # Payments
    # =========================

    base_payment: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    tmart_base_payment: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    additional_payments: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    adjustments: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    distance_payments: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    gross_total: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    # =========================
    # Bonuses
    # =========================

    referral_bonus: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    new_hire_bonus: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    weekly_bonus: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    extra_bonus: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2),
        nullable=True
    )

    # =========================
    # Company Deductions
    # =========================

    company_deductions: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    deduction_reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    # =========================
    # Transaction
    # =========================

    order_ref: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    transaction_date: Mapped[date | None] = mapped_column(
        Date,
        nullable=True
    )

    # =========================
    # Deductions / Adjustments
    # =========================

    advances: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    equipment_deduction: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    previous_debt: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    security_check_fee: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    penalty: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    penalty_reason: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    solidarity_fund: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    withheld_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    rent: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    office_dues: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    already_deducted: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    # =========================
    # Final Salary
    # =========================

    net_after_adjustments: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    remaining_balance: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    wallet_transfer_amount: Mapped[Decimal | None] = mapped_column(
        Numeric(12, 2),
        nullable=True
    )

    # =========================
    # Notes / Status
    # =========================

    transactions_note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    checking_status: Mapped[str | None] = mapped_column(
        String,
        nullable=True
    )

    note: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    # =========================
    # Timestamps
    # =========================

    created_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=func.now()
    )

    updated_at: Mapped[datetime | None] = mapped_column(
        DateTime,
        nullable=True,
        server_default=func.now(),
        onupdate=func.now()
    )

    # =========================
    # Composite Primary Key
    # =========================

    __table_args__ = (
        PrimaryKeyConstraint(
            "user_id",
            "payroll_year",
            "payroll_month",
            "payroll_week",
            name="pk_salary_details"
        ),
    )