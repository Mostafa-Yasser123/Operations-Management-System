from datetime import date

from sqlalchemy.orm import Session

from app.modules.custody.model import Custody
from app.modules.custody.repository import CustodyRepository
from app.modules.custody.schema import (
    CustodyCreate,
    CustodyUpdate,
)

from app.modules.users.repository import UserRepository


class CustodyService:

    def __init__(self):
        self.repository = CustodyRepository()
        self.user_repository = UserRepository()

    # =========================
    # Create Custody
    # =========================

    def create_custody(
        self,
        db: Session,
        custody_data: CustodyCreate
    ):

        # =========================
        # Check User
        # =========================

        user = self.user_repository.get_by_id(
            db,
            custody_data.user_id
        )

        if not user:
            raise ValueError("User not found")

        # =========================
        # Check Duplicate
        # =========================

        existing_custody = self.repository.get_by_key(
            db,
            custody_data.user_id,
            custody_data.week_name,
            custody_data.payment_date
        )

        if existing_custody:
            raise ValueError(
                "Custody record already exists for this user, week and payment date"
            )

        # =========================
        # Create Custody
        # =========================

        new_custody = Custody(
            **custody_data.model_dump()
        )

        return self.repository.create(
            db,
            new_custody
        )

    # =========================
    # Get All Custody
    # =========================

    def get_all_custody(
        self,
        db: Session
    ):

        return self.repository.get_all(db)

    # =========================
    # Get Custody
    # =========================

    def get_custody(
        self,
        db: Session,
        user_id: str,
        week_name: str,
        payment_date: date
    ):

        custody = self.repository.get_by_key(
            db,
            user_id,
            week_name,
            payment_date
        )

        if not custody:
            raise ValueError(
                "Custody record not found"
            )

        return custody

    # =========================
    # Update Custody
    # =========================

    def update_custody(
        self,
        db: Session,
        user_id: str,
        week_name: str,
        payment_date: date,
        custody_data: CustodyUpdate
    ):

        custody = self.repository.get_by_key(
            db,
            user_id,
            week_name,
            payment_date
        )

        if not custody:
            raise ValueError(
                "Custody record not found"
            )

        # =========================
        # Update Fields
        # =========================

        update_data = custody_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                custody,
                field,
                value
            )

        return self.repository.update(
            db,
            custody
        )

    # =========================
    # Delete Custody
    # =========================

    def delete_custody(
        self,
        db: Session,
        user_id: str,
        week_name: str,
        payment_date: date
    ):

        custody = self.repository.get_by_key(
            db,
            user_id,
            week_name,
            payment_date
        )

        if not custody:
            raise ValueError(
                "Custody record not found"
            )

        self.repository.delete(
            db,
            custody
        )

        return {
            "message": "Custody record deleted successfully"
        }