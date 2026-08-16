from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.modules.users.schema import (
    UserCreate,
    UserResponse,
    UserTermination,
    UserUpdate,
)
from app.modules.users.service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
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


user_service = UserService()


# =========================
# Create User
# =========================
@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    try:
        return user_service.create_user(db, user)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# =========================
# Get All Users
# =========================
@router.get(
    "/",
    response_model=list[UserResponse],
)
def get_all_users(
    db: Session = Depends(get_db),
):
    return user_service.get_all_users(db)


# =========================
# Get User By ID
# =========================
@router.get(
    "/{user_id}",
    response_model=UserResponse,
)
def get_user_by_id(
    user_id: str,
    db: Session = Depends(get_db),
):
    try:
        return user_service.get_user_by_id(db, user_id)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )


# =========================
# Terminate User
# =========================
@router.patch(
    "/{user_id}/terminate",
    response_model=UserResponse,
)
def terminate_user(
    user_id: str,
    termination_data: UserTermination,
    db: Session = Depends(get_db),
):
    try:
        return user_service.terminate_user(
            db,
            user_id,
            termination_data,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
    
    
    # =========================
# Update User
# =========================

@router.patch(
    "/{user_id}",
    response_model=UserResponse,
)
def update_user(
    user_id: str,
    user_data: UserUpdate,
    db: Session = Depends(get_db),
):
    try:
        return user_service.update_user(
            db,
            user_id,
            user_data,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    
    
    # =========================
# Delete User
# =========================

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
)
def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
):
    try:
        return user_service.delete_user(
            db,
            user_id,
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )    