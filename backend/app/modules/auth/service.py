from sqlalchemy.orm import Session

from app.core.security import (
    verify_password,
      hash_password,
    create_access_token
)
from app.modules.users.repository import UserRepository
from app.modules.auth.schema import (
    LoginRequest,
    TokenResponse,
    ChangePasswordRequest,
    ResetPasswordRequest,
)


class AuthService:

    def __init__(self):
        self.user_repository = UserRepository()
        
    # =========================
    # Login
    # =========================
    
    def login(
        self,
        db: Session,
        login_data: LoginRequest
    ) -> TokenResponse:

        # =========================
        # Check Username
        # =========================

        user = self.user_repository.get_by_username(
            db,
            login_data.user_name
        )

        if not user:
            raise ValueError("Invalid username or password")

        # =========================
        # Check Password
        # =========================

        if not verify_password(
            login_data.password,
            user.hash_password
        ):
            raise ValueError("Invalid username or password")

        # =========================
        # Check User Status
        # =========================

        if not user.is_active:
            raise ValueError("User account is inactive")

        if user.is_termination:
            raise ValueError("User account is terminated")

        # =========================
        # Create JWT
        # =========================

        access_token = create_access_token(
            subject=user.id,
            extra_data={
                "role": user.role.value,
                "user_name": user.user_name
            }
        )

        return TokenResponse(
            access_token=access_token
        )
        
        # =========================
        # Change Password
        # =========================

    def change_password(
        self,
        db: Session,
        user,
        password_data: ChangePasswordRequest
      ):

        # Check current password
        if not verify_password(
        password_data.old_password,
        user.hash_password
      ):
          raise ValueError("Current password is incorrect")

        # Prevent same password
        if password_data.old_password == password_data.new_password:
          raise ValueError("New password must be different from current password")

        # Save new password
        user.hash_password = hash_password(
          password_data.new_password
      )

        db.commit()
        db.refresh(user)

        return {
          "message": "Password changed successfully"
      }
      
      # =========================
# Reset Password (Admin)
# =========================

def reset_password(
    self,
    db: Session,
    user_id: str,
    password_data: ResetPasswordRequest
):

    user = self.user_repository.get_by_id(
        db,
        user_id
    )

    if not user:
        raise ValueError("User not found")

    user.hash_password = hash_password(
        password_data.new_password
    )

    db.commit()
    db.refresh(user)

    return {
        "message": "Password reset successfully"
    }  
        