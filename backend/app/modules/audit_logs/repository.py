from sqlalchemy.orm import Session

from app.modules.audit_logs.model import AuditLog
from app.modules.users.model import User
from app.common.enums import UserRole

class AuditLogRepository:

    # =========================
    # Create
    # =========================

    def create(
        self,
        db: Session,
        audit_log: AuditLog
    ):
        db.add(audit_log)
        db.commit()
        db.refresh(audit_log)

        return audit_log

    # =========================
    # Get By Delivery ID
    # =========================

    def get_by_delivery_id(
        self,
        db: Session,
        delivery_id: str
    ):
        return (
            db.query(AuditLog)
            .filter(
                AuditLog.delivery_id == delivery_id
            )
            .first()
        )

    # =========================
    # Get All
    # =========================

    def get_all(
        self,
        db: Session
    ):
        return (
            db.query(AuditLog)
            .all()
        )
  
    # =========================
    # Get All Supervisors
    # =========================
    
    def get_all_supervisors(
        self,
        db: Session
    ):
        return (
            db.query(User)
            .filter(User.role == UserRole.SUPERVISOR)
            .all()
        ) 
  
    # =========================
    # Update
    # =========================

    def update(
        self,
        db: Session,
        audit_log: AuditLog
    ):
        db.commit()
        db.refresh(audit_log)

        return audit_log

    # =========================
    # Delete
    # =========================

    def delete(
        self,
        db: Session,
        audit_log: AuditLog
    ):
        db.delete(audit_log)
        db.commit()

