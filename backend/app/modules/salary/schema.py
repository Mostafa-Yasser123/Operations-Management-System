from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


# =========================
# Create
# =========================

class SalaryCreate(BaseModel):

    # =========================
    # Payroll
    # =========================

    user_id: str = Field(
        ...,
        min_length=1
    )

    payroll_year: int = Field(
        ...,
        ge=2000
    )

    payroll_month: int = Field(
        ...,
        ge=1,
        le=12
    )

    payroll_week: int = Field(
        ...,
        ge=1
    )

    # =========================
    # Rider Information
    # =========================

    week_label: Optional[str] = None

    rider_name: Optional[str] = None

    vehicle_type: Optional[str] = None

    smart_wallet: Optional[str] = None

    account_type: Optional[str] = None

    # =========================
    # Orders
    # =========================

    total_orders: Optional[int] = Field(
        None,
        ge=0
    )

    completed_orders: Optional[int] = Field(
        None,
        ge=0
    )

    pickup_orders: Optional[int] = Field(
        None,
        ge=0
    )

    delivery_orders: Optional[int] = Field(
        None,
        ge=0
    )

    cancelled_orders: Optional[int] = Field(
        None,
        ge=0
    )

    refunded_cancelled_orders: Optional[Decimal] = Field(
        None,
        ge=0
    )

    tmart_completed_orders: Optional[int] = Field(
        None,
        ge=0
    )

    tmart_pickup_orders: Optional[int] = Field(
        None,
        ge=0
    )

    tmart_delivery_orders: Optional[int] = Field(
        None,
        ge=0
    )

    tmart_cancelled_orders: Optional[int] = Field(
        None,
        ge=0
    )

    # =========================
    # Payments
    # =========================

    base_payment: Optional[Decimal] = None

    tmart_base_payment: Optional[Decimal] = None

    additional_payments: Optional[Decimal] = None

    adjustments: Optional[Decimal] = None

    distance_payments: Optional[Decimal] = None

    gross_total: Optional[Decimal] = None

    # =========================
    # Bonuses
    # =========================

    referral_bonus: Optional[Decimal] = None

    new_hire_bonus: Optional[Decimal] = None

    weekly_bonus: Optional[Decimal] = None

    extra_bonus: Optional[Decimal] = None

    # =========================
    # Company Deductions
    # =========================

    company_deductions: Optional[Decimal] = None

    deduction_reason: Optional[str] = None

    # =========================
    # Transaction
    # =========================

    order_ref: Optional[str] = None

    transaction_date: Optional[date] = None

    # =========================
    # Deductions / Adjustments
    # =========================

    advances: Optional[Decimal] = None

    equipment_deduction: Optional[Decimal] = None

    previous_debt: Optional[Decimal] = None

    security_check_fee: Optional[Decimal] = None

    penalty: Optional[Decimal] = None

    penalty_reason: Optional[str] = None

    solidarity_fund: Optional[Decimal] = None

    withheld_amount: Optional[Decimal] = None

    rent: Optional[Decimal] = None

    office_dues: Optional[Decimal] = None

    already_deducted: Optional[Decimal] = None

    # =========================
    # Final Salary
    # =========================

    net_after_adjustments: Optional[Decimal] = None

    remaining_balance: Optional[Decimal] = None

    wallet_transfer_amount: Optional[Decimal] = None

    # =========================
    # Notes / Status
    # =========================

    transactions_note: Optional[str] = None

    checking_status: Optional[str] = None

    note: Optional[str] = None


# =========================
# Update
# =========================

class SalaryUpdate(BaseModel):

    week_label: Optional[str] = None

    rider_name: Optional[str] = None

    vehicle_type: Optional[str] = None

    smart_wallet: Optional[str] = None

    account_type: Optional[str] = None

    total_orders: Optional[int] = Field(
        None,
        ge=0
    )

    completed_orders: Optional[int] = Field(
        None,
        ge=0
    )

    pickup_orders: Optional[int] = Field(
        None,
        ge=0
    )

    delivery_orders: Optional[int] = Field(
        None,
        ge=0
    )

    cancelled_orders: Optional[int] = Field(
        None,
        ge=0
    )

    refunded_cancelled_orders: Optional[Decimal] = Field(
        None,
        ge=0
    )

    tmart_completed_orders: Optional[int] = Field(
        None,
        ge=0
    )

    tmart_pickup_orders: Optional[int] = Field(
        None,
        ge=0
    )

    tmart_delivery_orders: Optional[int] = Field(
        None,
        ge=0
    )

    tmart_cancelled_orders: Optional[int] = Field(
        None,
        ge=0
    )

    base_payment: Optional[Decimal] = None

    tmart_base_payment: Optional[Decimal] = None

    additional_payments: Optional[Decimal] = None

    adjustments: Optional[Decimal] = None

    distance_payments: Optional[Decimal] = None

    gross_total: Optional[Decimal] = None

    referral_bonus: Optional[Decimal] = None

    new_hire_bonus: Optional[Decimal] = None

    weekly_bonus: Optional[Decimal] = None

    extra_bonus: Optional[Decimal] = None

    company_deductions: Optional[Decimal] = None

    deduction_reason: Optional[str] = None

    order_ref: Optional[str] = None

    transaction_date: Optional[date] = None

    advances: Optional[Decimal] = None

    equipment_deduction: Optional[Decimal] = None

    previous_debt: Optional[Decimal] = None

    security_check_fee: Optional[Decimal] = None

    penalty: Optional[Decimal] = None

    penalty_reason: Optional[str] = None

    solidarity_fund: Optional[Decimal] = None

    withheld_amount: Optional[Decimal] = None

    rent: Optional[Decimal] = None

    office_dues: Optional[Decimal] = None

    already_deducted: Optional[Decimal] = None

    net_after_adjustments: Optional[Decimal] = None

    remaining_balance: Optional[Decimal] = None

    wallet_transfer_amount: Optional[Decimal] = None

    transactions_note: Optional[str] = None

    checking_status: Optional[str] = None

    note: Optional[str] = None


# =========================
# Response
# =========================

class SalaryResponse(BaseModel):

    user_id: str

    payroll_year: int

    payroll_month: int

    payroll_week: int

    week_label: Optional[str]

    rider_name: Optional[str]

    vehicle_type: Optional[str]

    smart_wallet: Optional[str]

    account_type: Optional[str]

    total_orders: Optional[int]

    completed_orders: Optional[int]

    pickup_orders: Optional[int]

    delivery_orders: Optional[int]

    cancelled_orders: Optional[int]

    refunded_cancelled_orders: Optional[Decimal]

    tmart_completed_orders: Optional[int]

    tmart_pickup_orders: Optional[int]

    tmart_delivery_orders: Optional[int]

    tmart_cancelled_orders: Optional[int]

    base_payment: Optional[Decimal]

    tmart_base_payment: Optional[Decimal]

    additional_payments: Optional[Decimal]

    adjustments: Optional[Decimal]

    distance_payments: Optional[Decimal]

    gross_total: Optional[Decimal]

    referral_bonus: Optional[Decimal]

    new_hire_bonus: Optional[Decimal]

    weekly_bonus: Optional[Decimal]

    extra_bonus: Optional[Decimal]

    company_deductions: Optional[Decimal]

    deduction_reason: Optional[str]

    order_ref: Optional[str]

    transaction_date: Optional[date]

    advances: Optional[Decimal]

    equipment_deduction: Optional[Decimal]

    previous_debt: Optional[Decimal]

    security_check_fee: Optional[Decimal]

    penalty: Optional[Decimal]

    penalty_reason: Optional[str]

    solidarity_fund: Optional[Decimal]

    withheld_amount: Optional[Decimal]

    rent: Optional[Decimal]

    office_dues: Optional[Decimal]

    already_deducted: Optional[Decimal]

    net_after_adjustments: Optional[Decimal]

    remaining_balance: Optional[Decimal]

    wallet_transfer_amount: Optional[Decimal]

    transactions_note: Optional[str]

    checking_status: Optional[str]

    note: Optional[str]

    created_at: Optional[datetime]

    updated_at: Optional[datetime]

    class Config:
        from_attributes = True