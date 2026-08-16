from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.modules.users.model import User
from app.modules.users.repository import UserRepository
from app.modules.users.schema import (
    UserCreate,
    UserTermination,
    UserUpdate,
)


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    # =========================
    # Create User
    # =========================

    def create_user(
        self,
        db: Session,
        user_data: UserCreate
    ):

        if self.repository.get_by_id(db, user_data.id):
            raise ValueError("User ID already exists")

        if self.repository.get_by_username(db, user_data.user_name):
            raise ValueError("Username already exists")

        new_user = User(
            id=user_data.id,
            name=user_data.name,
            phone_number=user_data.phone_number,
            sp=user_data.sp,
            zone=user_data.zone,
            city=user_data.city,
            alt_phone_number=user_data.alt_phone_number,
            relation=user_data.relation,
            national_id_no=user_data.national_id_no,
            talabat_e_mail=user_data.talabat_e_mail,
            vehicle=user_data.vehicle,
            education=user_data.education,
            first_contract_date=user_data.first_contract_date,
            last_shift_date=user_data.last_shift_date,
            role=user_data.role,
            user_name=user_data.user_name,
            hash_password=hash_password(user_data.password),
            bike_number=user_data.bike_number,
            year=user_data.year,
            is_active=True,
            is_available=True,
            is_termination=False,
        )

        return self.repository.create(db, new_user)

    # =========================
    # Terminate User
    # =========================

    def terminate_user(
        self,
        db: Session,
        user_id: str,
        termination_data: UserTermination
    ):

        user = self.repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("User not found")

        if user.is_termination:
            raise ValueError("User is already terminated")

        user.is_termination = True
        user.is_active = False
        user.is_available = False
        user.last_shift_date = termination_data.last_shift_date
        user.termination_reason = termination_data.termination_reason

        db.commit()
        db.refresh(user)

        return user

    # =========================
    # Get User by ID
    # =========================

    def get_user_by_id(
        self,
        db: Session,
        user_id: str
    ):

        user = self.repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("User not found")

        return user

    # =========================
    # Get All Users
    # =========================

    def get_all_users(
        self,
        db: Session
    ):
        return self.repository.get_all(db)

    # =========================
    # Update User
    # =========================

    def update_user(
        self,
        db: Session,
        user_id: str,
        user_data: UserUpdate
    ):

        user = self.repository.get_by_id(db, user_id)

        if not user:
            raise ValueError("User not found")

        update_data = user_data.model_dump(exclude_unset=True)

        if (
            "user_name" in update_data
            and update_data["user_name"] != user.user_name
        ):
            existing = self.repository.get_by_username(
                db,
                update_data["user_name"]
            )

            if existing:
                raise ValueError("Username already exists")

        for field, value in update_data.items():
            setattr(user, field, value)

        db.commit()
        db.refresh(user)

        return user

    # =========================
    # Delete User
    # =========================

    def delete_user(
        self,
        db: Session,
        user_id: str
    ):

        user = self.repository.get_by_id(
            db,
            user_id
        )

        if not user:
            raise ValueError("User not found")

        self.repository.delete(
            db,
            user
        )

        return {
            "message": "User deleted successfully"
        }