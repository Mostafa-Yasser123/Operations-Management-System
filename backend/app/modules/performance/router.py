from datetime import date

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.modules.performance.schema import (
    PerformanceCreate,
    PerformanceUpdate,
    PerformanceResponse,
)

from app.modules.performance.service import PerformanceService


router = APIRouter(
    prefix="/performance",
    tags=["Performance"],
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


performance_service = PerformanceService()


# =========================
# Create Performance
# =========================

@router.post(
    "/",
    response_model=PerformanceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_performance(
    performance: PerformanceCreate,
    db: Session = Depends(get_db),
):
    try:
        return performance_service.create_performance(
            db,
            performance
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Get All Performance
# =========================

@router.get(
    "/",
    response_model=list[PerformanceResponse],
)
def get_all_performance(
    db: Session = Depends(get_db),
):
    return performance_service.get_all_performance(db)


# =========================
# Get Performance
# =========================

@router.get(
    "/{user_id}/{log_date}",
    response_model=PerformanceResponse,
)
def get_performance(
    user_id: str,
    log_date: date,
    db: Session = Depends(get_db),
):
    try:
        return performance_service.get_performance(
            db,
            user_id,
            log_date
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# =========================
# Update Performance
# =========================

@router.patch(
    "/{user_id}/{log_date}",
    response_model=PerformanceResponse,
)
def update_performance(
    user_id: str,
    log_date: date,
    performance: PerformanceUpdate,
    db: Session = Depends(get_db),
):
    try:
        return performance_service.update_performance(
            db,
            user_id,
            log_date,
            performance
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Delete Performance
# =========================

@router.delete(
    "/{user_id}/{log_date}"
)
def delete_performance(
    user_id: str,
    log_date: date,
    db: Session = Depends(get_db),
):
    try:
        return performance_service.delete_performance(
            db,
            user_id,
            log_date
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )