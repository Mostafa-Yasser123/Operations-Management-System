from sqlalchemy.orm import Session

from app.modules.performance.model import MasterPerformance


class PerformanceRepository:

    # =========================
    # Create
    # =========================

    def create(
        self,
        db: Session,
        performance: MasterPerformance
    ):

        db.add(performance)
        db.commit()
        db.refresh(performance)

        return performance

    # =========================
    # Get All
    # =========================

    def get_all(
        self,
        db: Session
    ):

        return db.query(MasterPerformance).all()

    # =========================
    # Get By Composite Key
    # =========================

    def get_by_key(
        self,
        db: Session,
        user_id: str,
        log_date
    ):

        return (
            db.query(MasterPerformance)
            .filter(
                MasterPerformance.user_id == user_id,
                MasterPerformance.log_date == log_date
            )
            .first()
        )

    # =========================
    # Update
    # =========================

    def update(
        self,
        db: Session,
        performance: MasterPerformance
    ):

        db.commit()
        db.refresh(performance)

        return performance

    # =========================
    # Delete
    # =========================

    def delete(
        self,
        db: Session,
        performance: MasterPerformance
    ):

        db.delete(performance)
        db.commit()

        return performance