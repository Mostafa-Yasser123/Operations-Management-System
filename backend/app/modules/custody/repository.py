from datetime import date

from sqlalchemy.orm import Session

from app.modules.custody.model import Custody


class CustodyRepository:

    # =========================
    # Create
    # =========================

    def create(
        self,
        db: Session,
        custody: Custody
    ):

        db.add(custody)
        db.commit()
        db.refresh(custody)

        return custody

    # =========================
    # Get All
    # =========================

    def get_all(
        self,
        db: Session
    ):

        return (
            db.query(Custody)
            .all()
        )

    # =========================
    # Get By Composite Key
    # =========================

    def get_by_key(
        self,
        db: Session,
        user_id: str,
        week_name: str,
        payment_date: date
    ):

        return (
            db.query(Custody)
            .filter(
                Custody.user_id == user_id,
                Custody.week_name == week_name,
                Custody.payment_date == payment_date
            )
            .first()
        )

    # =========================
    # Update
    # =========================

    def update(
        self,
        db: Session,
        custody: Custody
    ):

        db.commit()
        db.refresh(custody)

        return custody

    # =========================
    # Delete
    # =========================

    def delete(
        self,
        db: Session,
        custody: Custody
    ):

        db.delete(custody)
        db.commit()

        return custody