from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.modules.store.schema import (
    StoreCreate,
    StoreUpdate,
    StoreResponse,
)

from app.modules.store.service import StoreService


router = APIRouter(
    prefix="/store",
    tags=["Store"],
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


store_service = StoreService()


# =========================
# Create Item
# =========================

@router.post(
    "/",
    response_model=StoreResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_item(
    item: StoreCreate,
    db: Session = Depends(get_db),
):

    try:
        return store_service.create_item(
            db,
            item
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# =========================
# Get All Items
# =========================

@router.get(
    "/",
    response_model=list[StoreResponse],
)
def get_all_items(
    db: Session = Depends(get_db),
):

    return store_service.get_all_items(db)


# =========================
# Get Item By ID
# =========================

@router.get(
    "/{item_id}",
    response_model=StoreResponse,
)
def get_item_by_id(
    item_id: int,
    db: Session = Depends(get_db),
):

    try:
        return store_service.get_item_by_id(
            db,
            item_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# =========================
# Update Item
# =========================

@router.patch(
    "/{item_id}",
    response_model=StoreResponse,
)
def update_item(
    item_id: int,
    item: StoreUpdate,
    db: Session = Depends(get_db),
):

    try:
        return store_service.update_item(
            db,
            item_id,
            item
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# =========================
# Delete Item
# =========================

@router.delete(
    "/{item_id}",
)
def delete_item(
    item_id: int,
    db: Session = Depends(get_db),
):

    try:
        return store_service.delete_item(
            db,
            item_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )