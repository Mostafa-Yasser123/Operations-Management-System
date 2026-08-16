from sqlalchemy.orm import Session

from app.modules.salary.model import SalaryDetail
from app.modules.salary.repository import SalaryRepository
from app.modules.salary.schema import (
    SalaryCreate,
    SalaryUpdate,
)

from app.modules.users.repository import UserRepository


class SalaryService:

    def __init__(self):
        self.repository = SalaryRepository()
        self.user_repository = UserRepository()

    # =========================
    # Create Salary
    # =========================

    def create_salary(
        self,
        db: Session,
        salary_data: SalaryCreate
    ):

        # =========================
        # Check User
        # =========================

        user = self.user_repository.get_by_id(
            db,
            salary_data.user_id
        )

        if not user:
            raise ValueError("User not found")

        # =========================
        # Check Duplicate
        # =========================

        existing_salary = self.repository.get_by_key(
            db,
            salary_data.user_id,
            salary_data.payroll_year,
            salary_data.payroll_month,
            salary_data.payroll_week
        )

        if existing_salary:
            raise ValueError(
                "Salary record already exists for this user and payroll week"
            )

        # =========================
        # Create Salary
        # =========================

        new_salary = SalaryDetail(
            **salary_data.model_dump()
        )

        return self.repository.create(
            db,
            new_salary
        )

    # =========================
    # Get All Salary
    # =========================

    def get_all_salary(
        self,
        db: Session
    ):

        return self.repository.get_all(db)

    # =========================
    # Get Salary
    # =========================

    def get_salary(
        self,
        db: Session,
        user_id: str,
        payroll_year: int,
        payroll_month: int,
        payroll_week: int
    ):

        salary = self.repository.get_by_key(
            db,
            user_id,
            payroll_year,
            payroll_month,
            payroll_week
        )

        if not salary:
            raise ValueError(
                "Salary record not found"
            )

        return salary

    # =========================
    # Update Salary
    # =========================

    def update_salary(
        self,
        db: Session,
        user_id: str,
        payroll_year: int,
        payroll_month: int,
        payroll_week: int,
        salary_data: SalaryUpdate
    ):

        salary = self.repository.get_by_key(
            db,
            user_id,
            payroll_year,
            payroll_month,
            payroll_week
        )

        if not salary:
            raise ValueError(
                "Salary record not found"
            )

        # =========================
        # Update Fields
        # =========================

        update_data = salary_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(
                salary,
                field,
                value
            )

        return self.repository.update(
            db,
            salary
        )

    # =========================
    # Delete Salary
    # =========================

    def delete_salary(
        self,
        db: Session,
        user_id: str,
        payroll_year: int,
        payroll_month: int,
        payroll_week: int
    ):

        salary = self.repository.get_by_key(
            db,
            user_id,
            payroll_year,
            payroll_month,
            payroll_week
        )

        if not salary:
            raise ValueError(
                "Salary record not found"
            )

        self.repository.delete(
            db,
            salary
        )

        return {
            "message": "Salary record deleted successfully"
        }