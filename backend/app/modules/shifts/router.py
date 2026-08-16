from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.modules.shifts.schema import (
    ShiftCreate,
    ShiftUpdate,
    ShiftResponse,
)

from app.modules.shifts.service import ShiftService


router = APIRouter(
    prefix="/shifts",
    tags=["Shifts"],
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


shift_service = ShiftService()


# =========================
# Create Shift
# =========================

@router.post(
    "/",
    response_model=ShiftResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_shift(
    shift: ShiftCreate,
    db: Session = Depends(get_db),
):
    try:
        return shift_service.create_shift(
            db,
            shift
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Get All Shifts
# =========================

@router.get(
    "/",
    response_model=list[ShiftResponse],
)
def get_all_shifts(
    db: Session = Depends(get_db),
):
    return shift_service.get_all_shifts(db)


# =========================
# Get Shift
# =========================

@router.get(
    "/{user_id}/{shift_date}",
    response_model=ShiftResponse,
)
def get_shift(
    user_id: str,
    shift_date: date,
    db: Session = Depends(get_db),
):
    try:
        return shift_service.get_shift(
            db,
            user_id,
            shift_date
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# =========================
# Update Shift
# =========================

@router.patch(
    "/{user_id}/{shift_date}",
    response_model=ShiftResponse,
)
def update_shift(
    user_id: str,
    shift_date: date,
    shift: ShiftUpdate,
    db: Session = Depends(get_db),
):
    try:
        return shift_service.update_shift(
            db,
            user_id,
            shift_date,
            shift
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Delete Shift
# =========================

@router.delete(
    "/{user_id}/{shift_date}"
)
def delete_shift(
    user_id: str,
    shift_date: date,
    db: Session = Depends(get_db),
):
    try:
        return shift_service.delete_shift(
            db,
            user_id,
            shift_date
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )