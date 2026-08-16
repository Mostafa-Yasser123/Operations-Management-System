
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from app.database.session import SessionLocal

from app.modules.audit_logs.schema import (
    AuditLogCreate,
    AuditLogUpdate,
    AuditLogResponse,
)

from app.modules.audit_logs.service import AuditLogService


router = APIRouter(
    prefix="/audit-logs",
    tags=["Audit Logs"],
)


# =========================
# Database Dependency
# =========================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


audit_log_service = AuditLogService()


# =========================
# Create Audit Log
# =========================

@router.post(
    "/",
    response_model=AuditLogResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_audit_log(
    audit_log: AuditLogCreate,
    db: Session = Depends(get_db),
):

    try:

        return audit_log_service.create_audit_log(
            db,
            audit_log
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Get All Audit Logs
# =========================

@router.get(
    "/",
    response_model=list[AuditLogResponse],
)
def get_all_audit_logs(
    db: Session = Depends(get_db),
):

    return audit_log_service.get_all_audit_logs(
        db
    )


# =========================
# Get All Supervisors
# =========================

@router.get(
    "/supervisors"
)
def get_all_supervisors(
    db: Session = Depends(get_db),
):
    return audit_log_service.get_all_supervisors(db)

# =========================
# Get Audit Log
# =========================

@router.get(
    "/{delivery_id}",
    response_model=AuditLogResponse,
)
def get_audit_log(
    delivery_id: str,
    db: Session = Depends(get_db),
):

    try:

        return audit_log_service.get_audit_log(
            db,
            delivery_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


# =========================
# Update Audit Log
# =========================

@router.patch(
    "/{delivery_id}",
    response_model=AuditLogResponse,
)
def update_audit_log(
    delivery_id: str,
    audit_log: AuditLogUpdate,
    db: Session = Depends(get_db),
):

    try:

        return audit_log_service.update_audit_log(
            db,
            delivery_id,
            audit_log
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )


# =========================
# Delete Audit Log
# =========================

@router.delete(
    "/{delivery_id}",
)
def delete_audit_log(
    delivery_id: str,
    db: Session = Depends(get_db),
):

    try:

        return audit_log_service.delete_audit_log(
            db,
            delivery_id
        )

    except ValueError as e:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )

