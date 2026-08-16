from sqlalchemy.orm import Session

from app.modules.performance.model import MasterPerformance
from app.modules.performance.repository import PerformanceRepository
from app.modules.performance.schema import (
    PerformanceCreate,
    PerformanceUpdate,
)

from app.modules.users.repository import UserRepository


class PerformanceService:

    def __init__(self):
        self.repository = PerformanceRepository()
        self.user_repository = UserRepository()

    # =========================
    # Create Performance
    # =========================

    def create_performance(
        self,
        db: Session,
        performance_data: PerformanceCreate
    ):

        # =========================
        # Check User
        # =========================

        user = self.user_repository.get_by_id(
            db,
            performance_data.user_id
        )

        if not user:
            raise ValueError("User not found")

        # =========================
        # Check Duplicate
        # =========================

        existing_performance = self.repository.get_by_key(
            db,
            performance_data.user_id,
            performance_data.log_date
        )

        if existing_performance:
            raise ValueError(
                "Performance already exists for this user on this date"
            )

        # =========================
        # Create Performance
        # =========================

        new_performance = MasterPerformance(
            user_id=performance_data.user_id,
            log_date=performance_data.log_date,
            orders=performance_data.orders,
            hours=performance_data.hours,
            acceptance_rate=performance_data.acceptance_rate
        )

        return self.repository.create(
            db,
            new_performance
        )

    # =========================
    # Get All Performance
    # =========================

    def get_all_performance(
        self,
        db: Session
    ):

        return self.repository.get_all(db)

    # =========================
    # Get Performance
    # =========================

    def get_performance(
        self,
        db: Session,
        user_id: str,
        log_date
    ):

        performance = self.repository.get_by_key(
            db,
            user_id,
            log_date
        )

        if not performance:
            raise ValueError(
                "Performance not found"
            )

        return performance

    # =========================
    # Update Performance
    # =========================

    def update_performance(
        self,
        db: Session,
        user_id: str,
        log_date,
        performance_data: PerformanceUpdate
    ):

        performance = self.repository.get_by_key(
            db,
            user_id,
            log_date
        )

        if not performance:
            raise ValueError(
                "Performance not found"
            )

        # =========================
        # Update Fields
        # =========================

        update_data = performance_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                performance,
                field,
                value
            )

        return self.repository.update(
            db,
            performance
        )

    # =========================
    # Delete Performance
    # =========================

    def delete_performance(
        self,
        db: Session,
        user_id: str,
        log_date
    ):

        performance = self.repository.get_by_key(
            db,
            user_id,
            log_date
        )

        if not performance:
            raise ValueError(
                "Performance not found"
            )

        self.repository.delete(
            db,
            performance
        )

        return {
            "message": "Performance deleted successfully"
        }