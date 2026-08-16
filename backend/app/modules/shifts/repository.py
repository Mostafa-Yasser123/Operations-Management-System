from sqlalchemy.orm import Session

from app.modules.shifts.model import Shift


class ShiftRepository:

    # =========================
    # Create
    # =========================

    def create(
        self,
        db: Session,
        shift: Shift
    ):

        db.add(shift)
        db.commit()
        db.refresh(shift)

        return shift

    # =========================
    # Get All
    # =========================

    def get_all(
        self,
        db: Session
    ):

        return db.query(Shift).all()

    # =========================
    # Get By Composite Key
    # =========================

    def get_by_key(
        self,
        db: Session,
        user_id: str,
        shift_date
    ):

        return (
            db.query(Shift)
            .filter(
                Shift.user_id == user_id,
                Shift.shift_date == shift_date
            )
            .first()
        )

    # =========================
    # Update
    # =========================

    def update(
        self,
        db: Session,
        shift: Shift
    ):

        db.commit()
        db.refresh(shift)

        return shift

    # =========================
    # Delete
    # =========================

    def delete(
        self,
        db: Session,
        shift: Shift
    ):

        db.delete(shift)
        db.commit()

        return shift