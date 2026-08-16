from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.modules.custody.schema import (
    CustodyCreate,
    CustodyUpdate,
    CustodyResponse,
)

from app.modules.custody.service import CustodyService


router = APIRouter(
    prefix="/custody",
    tags=["Custody"],
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


custody_service = CustodyService()


# =========================
# Create Custody
# =========================

@router.post(
    "/",
    response_model=CustodyResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_custody(
    custody: CustodyCreate,
    db: Session = Depends(get_db),
):
    try:
        return custody_service.create_custody(
            db,
            custody
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Get All Custody
# =========================

@router.get(
    "/",
    response_model=list[CustodyResponse],
)
def get_all_custody(
    db: Session = Depends(get_db),
):
    return custody_service.get_all_custody(db)


# =========================
# Get Custody
# =========================

@router.get(
    "/{user_id}/{week_name}/{payment_date}",
    response_model=CustodyResponse,
)
def get_custody(
    user_id: str,
    week_name: str,
    payment_date: date,
    db: Session = Depends(get_db),
):
    try:
        return custody_service.get_custody(
            db,
            user_id,
            week_name,
            payment_date
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# =========================
# Update Custody
# =========================

@router.patch(
    "/{user_id}/{week_name}/{payment_date}",
    response_model=CustodyResponse,
)
def update_custody(
    user_id: str,
    week_name: str,
    payment_date: date,
    custody: CustodyUpdate,
    db: Session = Depends(get_db),
):
    try:
        return custody_service.update_custody(
            db,
            user_id,
            week_name,
            payment_date,
            custody
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Delete Custody
# =========================

@router.delete(
    "/{user_id}/{week_name}/{payment_date}"
)
def delete_custody(
    user_id: str,
    week_name: str,
    payment_date: date,
    db: Session = Depends(get_db),
):
    try:
        return custody_service.delete_custody(
            db,
            user_id,
            week_name,
            payment_date
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )