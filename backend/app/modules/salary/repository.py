from sqlalchemy.orm import Session

from app.modules.salary.model import SalaryDetail


class SalaryRepository:

    # =========================
    # Create
    # =========================

    def create(
        self,
        db: Session,
        salary: SalaryDetail
    ):

        db.add(salary)
        db.commit()
        db.refresh(salary)

        return salary

    # =========================
    # Get All
    # =========================

    def get_all(
        self,
        db: Session
    ):

        return (
            db.query(SalaryDetail)
            .all()
        )

    # =========================
    # Get By Composite Key
    # =========================

    def get_by_key(
        self,
        db: Session,
        user_id: str,
        payroll_year: int,
        payroll_month: int,
        payroll_week: int
    ):

        return (
            db.query(SalaryDetail)
            .filter(
                SalaryDetail.user_id == user_id,
                SalaryDetail.payroll_year == payroll_year,
                SalaryDetail.payroll_month == payroll_month,
                SalaryDetail.payroll_week == payroll_week
            )
            .first()
        )

    # =========================
    # Update
    # =========================

    def update(
        self,
        db: Session,
        salary: SalaryDetail
    ):

        db.commit()
        db.refresh(salary)

        return salary

    # =========================
    # Delete
    # =========================

    def delete(
        self,
        db: Session,
        salary: SalaryDetail
    ):

        db.delete(salary)
        db.commit()

        return salary