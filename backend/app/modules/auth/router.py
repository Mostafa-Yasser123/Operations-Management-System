from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import (
    get_db,
    get_current_user
)
from app.modules.auth.schema import (
    LoginRequest,
    TokenResponse,
    ChangePasswordRequest,
    ResetPasswordRequest,
)
from app.modules.auth.service import AuthService
from app.modules.users.model import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

auth_service = AuthService()

# =========================
# Login
# =========================

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    login_data: LoginRequest,
    db: Session = Depends(get_db)
):
    return auth_service.login(
        db,
        login_data
    )


# =========================
# Change Password
# =========================

@router.patch("/change-password")
def change_password(
    password_data: ChangePasswordRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return auth_service.change_password(
        db,
        current_user,
        password_data
    )
    
  # =========================
# Reset Password (Admin)
# =========================

@router.patch("/reset-password/{user_id}")
def reset_password(
    user_id: str,
    password_data: ResetPasswordRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # مؤقتًا أي مستخدم مسجل دخول يقدر ينفذها
    # في الخطوة القادمة هنخليها Administrator فقط

    return auth_service.reset_password(
        db,
        user_id,
        password_data
    )  