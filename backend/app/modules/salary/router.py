from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.modules.salary.schema import (
    SalaryCreate,
    SalaryUpdate,
    SalaryResponse,
)

from app.modules.salary.service import SalaryService


router = APIRouter(
    prefix="/salary",
    tags=["Salary"],
)


# =========================
# Database Dependency
# =========================

def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


salary_service = SalaryService()


# =========================
# Create Salary
# =========================

@router.post(
    "/",
    response_model=SalaryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_salary(
    salary: SalaryCreate,
    db: Session = Depends(get_db),
):
    try:
        return salary_service.create_salary(
            db,
            salary
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Get All Salary
# =========================

@router.get(
    "/",
    response_model=list[SalaryResponse],
)
def get_all_salary(
    db: Session = Depends(get_db),
):
    return salary_service.get_all_salary(db)


# =========================
# Get Salary
# =========================

@router.get(
    "/{user_id}/{payroll_year}/{payroll_month}/{payroll_week}",
    response_model=SalaryResponse,
)
def get_salary(
    user_id: str,
    payroll_year: int,
    payroll_month: int,
    payroll_week: int,
    db: Session = Depends(get_db),
):
    try:
        return salary_service.get_salary(
            db,
            user_id,
            payroll_year,
            payroll_month,
            payroll_week
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# =========================
# Update Salary
# =========================

@router.patch(
    "/{user_id}/{payroll_year}/{payroll_month}/{payroll_week}",
    response_model=SalaryResponse,
)
def update_salary(
    user_id: str,
    payroll_year: int,
    payroll_month: int,
    payroll_week: int,
    salary: SalaryUpdate,
    db: Session = Depends(get_db),
):
    try:
        return salary_service.update_salary(
            db,
            user_id,
            payroll_year,
            payroll_month,
            payroll_week,
            salary
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Delete Salary
# =========================

@router.delete(
    "/{user_id}/{payroll_year}/{payroll_month}/{payroll_week}"
)
def delete_salary(
    user_id: str,
    payroll_year: int,
    payroll_month: int,
    payroll_week: int,
    db: Session = Depends(get_db),
):
    try:
        return salary_service.delete_salary(
            db,
            user_id,
            payroll_year,
            payroll_month,
            payroll_week
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )