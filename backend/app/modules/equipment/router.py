
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.modules.equipment.schema import (
    EquipmentCreate,
    EquipmentUpdate,
    EquipmentResponse,
)

from app.modules.equipment.service import EquipmentService


router = APIRouter(
    prefix="/equipment",
    tags=["Equipment"],
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


equipment_service = EquipmentService()


# =========================
# Create Equipment
# =========================

@router.post(
    "/",
    response_model=EquipmentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_equipment(
    equipment: EquipmentCreate,
    db: Session = Depends(get_db),
):
    try:
        return equipment_service.create_equipment(
            db,
            equipment
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Get All Equipment
# =========================

@router.get(
    "/",
    response_model=list[EquipmentResponse],
)
def get_all_equipment(
    db: Session = Depends(get_db),
):
    return equipment_service.get_all_equipment(db)


# =========================
# Update Equipment
# =========================

@router.patch(
    "/{user_id}/{store_item_id}",
    response_model=EquipmentResponse,
)
def update_equipment(
    user_id: str,
    store_item_id: int,
    equipment: EquipmentUpdate,
    db: Session = Depends(get_db),
):
    try:
        return equipment_service.update_equipment(
            db,
            user_id,
            store_item_id,
            equipment
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Delete Equipment
# =========================

@router.delete(
    "/{user_id}/{store_item_id}"
)
def delete_equipment(
    user_id: str,
    store_item_id: int,
    db: Session = Depends(get_db),
):
    try:
        return equipment_service.delete_equipment(
            db,
            user_id,
            store_item_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

