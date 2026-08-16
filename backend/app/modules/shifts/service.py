from sqlalchemy.orm import Session

from app.modules.shifts.model import Shift
from app.modules.shifts.repository import ShiftRepository
from app.modules.shifts.schema import (
    ShiftCreate,
    ShiftUpdate,
)

from app.modules.users.repository import UserRepository


class ShiftService:

    def __init__(self):
        self.repository = ShiftRepository()
        self.user_repository = UserRepository()

    # =========================
    # Create Shift
    # =========================

    def create_shift(
        self,
        db: Session,
        shift_data: ShiftCreate
    ):

        # Check User
        user = self.user_repository.get_by_id(
            db,
            shift_data.user_id
        )

        if not user:
            raise ValueError("User not found")

        # Check if shift already exists
        existing_shift = self.repository.get_by_key(
            db,
            shift_data.user_id,
            shift_data.shift_date
        )

        if existing_shift:
            raise ValueError(
                "Shift already exists for this user on this date"
            )

        # Create Shift
        new_shift = Shift(
            user_id=shift_data.user_id,
            shift_date=shift_data.shift_date,
            start_time=shift_data.start_time,
            end_time=shift_data.end_time
        )

        return self.repository.create(
            db,
            new_shift
        )

    # =========================
    # Get All Shifts
    # =========================

    def get_all_shifts(
        self,
        db: Session
    ):

        return self.repository.get_all(db)

    # =========================
    # Get Shift By Composite Key
    # =========================

    def get_shift(
        self,
        db: Session,
        user_id: str,
        shift_date
    ):

        shift = self.repository.get_by_key(
            db,
            user_id,
            shift_date
        )

        if not shift:
            raise ValueError("Shift not found")

        return shift

    # =========================
    # Update Shift
    # =========================

    def update_shift(
        self,
        db: Session,
        user_id: str,
        shift_date,
        shift_data: ShiftUpdate
    ):

        shift = self.repository.get_by_key(
            db,
            user_id,
            shift_date
        )

        if not shift:
            raise ValueError("Shift not found")

        update_data = shift_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                shift,
                field,
                value
            )

        return self.repository.update(
            db,
            shift
        )

    # =========================
    # Delete Shift
    # =========================

    def delete_shift(
        self,
        db: Session,
        user_id: str,
        shift_date
    ):

        shift = self.repository.get_by_key(
            db,
            user_id,
            shift_date
        )

        if not shift:
            raise ValueError("Shift not found")

        self.repository.delete(
            db,
            shift
        )

        return {
            "message": "Shift deleted successfully"
        }