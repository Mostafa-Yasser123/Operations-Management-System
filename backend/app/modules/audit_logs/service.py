from sqlalchemy.orm import Session

from app.modules.audit_logs.model import AuditLog
from app.modules.audit_logs.repository import AuditLogRepository
from app.modules.audit_logs.schema import (
    AuditLogCreate,
    AuditLogUpdate,
)

from app.modules.users.repository import UserRepository


class AuditLogService:

    def __init__(self):
        self.repository = AuditLogRepository()
        self.user_repository = UserRepository()

    # =========================
    # Create Audit Log
    # =========================

    def create_audit_log(
        self,
        db: Session,
        audit_log_data: AuditLogCreate
    ):

        # =========================
        # Check Supervisor
        # =========================

        supervisor = self.user_repository.get_by_id(
            db,
            audit_log_data.supervisor_id
        )

        if not supervisor:
            raise ValueError("Supervisor not found")

        if supervisor.role.value != "supervisor":
            raise ValueError(
                "User is not a supervisor"
            )

        # =========================
        # Check Delivery Rider
        # =========================

        delivery = self.user_repository.get_by_id(
            db,
            audit_log_data.delivery_id
        )

        if not delivery:
            raise ValueError("Delivery rider not found")

        if delivery.role.value != "delivery":
            raise ValueError(
                "User is not a delivery rider"
            )

        # =========================
        # Check Existing Assignment
        # =========================

        existing = self.repository.get_by_delivery_id(
            db,
            audit_log_data.delivery_id
        )

        if existing:
            raise ValueError(
                "Delivery rider already has a supervisor"
            )

        # =========================
        # Create
        # =========================

        new_audit_log = AuditLog(
            supervisor_id=supervisor.id,
            delivery_id=delivery.id,
            delivery_name=delivery.name
        )

        return self.repository.create(
            db,
            new_audit_log
        )

    # =========================
    # Get All
    # =========================

    def get_all_audit_logs(
        self,
        db: Session
    ):
        return self.repository.get_all(db)
      
    def get_all_supervisors(
        self,
      db: Session
    ):
      return self.repository.get_all_supervisors(db)  

    # =========================
    # Get By Delivery ID
    # =========================

    def get_audit_log(
        self,
        db: Session,
        delivery_id: str
    ):

        audit_log = self.repository.get_by_delivery_id(
            db,
            delivery_id
        )

        if not audit_log:
            raise ValueError(
                "Audit log not found"
            )

        return audit_log

    # =========================
    # Update
    # =========================

    def update_audit_log(
        self,
        db: Session,
        delivery_id: str,
        audit_log_data: AuditLogUpdate
    ):

        # =========================
        # Get Existing Assignment
        # =========================

        audit_log = self.repository.get_by_delivery_id(
            db,
            delivery_id
        )

        if not audit_log:
            raise ValueError(
                "Audit log not found"
            )

        # =========================
        # Check New Supervisor
        # =========================

        supervisor = self.user_repository.get_by_id(
            db,
            audit_log_data.supervisor_id
        )

        if not supervisor:
            raise ValueError(
                "Supervisor not found"
            )

        if supervisor.role.value != "supervisor":
            raise ValueError(
                "User is not a supervisor"
            )

        # =========================
        # Update
        # =========================

        audit_log.supervisor_id = supervisor.id
        audit_log.delivery_name = audit_log_data.delivery_name

        return self.repository.update(
            db,
            audit_log
        )

    # =========================
    # Delete
    # =========================

    def delete_audit_log(
        self,
        db: Session,
        delivery_id: str
    ):

        audit_log = self.repository.get_by_delivery_id(
            db,
            delivery_id
        )

        if not audit_log:
            raise ValueError(
                "Audit log not found"
            )

        self.repository.delete(
            db,
            audit_log
        )

        return {
            "message": "Audit log deleted successfully"
        }

