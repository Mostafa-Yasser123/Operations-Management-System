
from sqlalchemy.orm import Session

from app.modules.equipment.model import Equipment


class EquipmentRepository:

    # =========================
    # Create
    # =========================

    def create(
        self,
        db: Session,
        equipment: Equipment
    ):
        db.add(equipment)
        db.commit()
        db.refresh(equipment)

        return equipment

    # =========================
    # Get By Composite Key
    # =========================

    def get_by_key(
        self,
        db: Session,
        user_id: str,
        store_item_id: int
    ):
        return (
            db.query(Equipment)
            .filter(
                Equipment.user_id == user_id,
                Equipment.store_item_id == store_item_id
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
        return db.query(Equipment).all()

    # =========================
    # Update
    # =========================

    def update(
        self,
        db: Session,
        equipment: Equipment
    ):
        db.commit()
        db.refresh(equipment)

        return equipment

    # =========================
    # Delete
    # =========================

    def delete(
        self,
        db: Session,
        equipment: Equipment
    ):
        db.delete(equipment)
        db.commit()

