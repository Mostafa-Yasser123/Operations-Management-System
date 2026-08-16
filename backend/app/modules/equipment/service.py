
from decimal import Decimal

from sqlalchemy.orm import Session

from app.modules.equipment.model import Equipment
from app.modules.equipment.repository import EquipmentRepository
from app.modules.equipment.schema import (
    EquipmentCreate,
    EquipmentUpdate,
)

from app.modules.users.repository import UserRepository
from app.modules.store.repository import StoreRepository


class EquipmentService:

    def __init__(self):
        self.repository = EquipmentRepository()
        self.user_repository = UserRepository()
        self.store_repository = StoreRepository()

    # =========================
    # Create Equipment
    # =========================

    def create_equipment(
        self,
        db: Session,
        equipment_data: EquipmentCreate
    ):

        # Check User
        user = self.user_repository.get_by_id(
            db,
            equipment_data.user_id
        )

        if not user:
            raise ValueError("User not found")

        # Check Store Item
        item = self.store_repository.get_by_id(
            db,
            equipment_data.store_item_id
        )

        if not item:
            raise ValueError("Store item not found")

        # Check Quantity
        if equipment_data.quantity > item.quantity:
            raise ValueError("Not enough quantity in store")

        # Calculate price
        unit_price = Decimal(str(item.unit_value))

        total_value = (
            unit_price *
            equipment_data.quantity
        )

        # Create Equipment
        new_equipment = Equipment(
            user_id=equipment_data.user_id,
            store_item_id=equipment_data.store_item_id,
            quantity=equipment_data.quantity,
            unit_price=unit_price,
            total_value=total_value,
            issue_date=equipment_data.issue_date
        )

        # Deduct quantity from store
        item.quantity -= equipment_data.quantity

        return self.repository.create(
            db,
            new_equipment
        )

    # =========================
    # Get All
    # =========================

    def get_all_equipment(
        self,
        db: Session
    ):
        return self.repository.get_all(db)

    # =========================
    # Get Equipment
    # =========================

    def get_equipment(
        self,
        db: Session,
        user_id: str,
        store_item_id: int
    ):

        equipment = self.repository.get_by_key(
            db,
            user_id,
            store_item_id
        )

        if not equipment:
            raise ValueError("Equipment not found")

        return equipment

    # =========================
    # Update
    # =========================

    def update_equipment(
        self,
        db: Session,
        user_id: str,
        store_item_id: int,
        equipment_data: EquipmentUpdate
    ):

        equipment = self.repository.get_by_key(
            db,
            user_id,
            store_item_id
        )

        if not equipment:
            raise ValueError("Equipment not found")

        update_data = equipment_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(equipment, field, value)

        # Recalculate total value
        equipment.total_value = (
            equipment.quantity *
            equipment.unit_price
        )

        return self.repository.update(
            db,
            equipment
        )

    # =========================
    # Delete
    # =========================

    def delete_equipment(
        self,
        db: Session,
        user_id: str,
        store_item_id: int
    ):

        equipment = self.repository.get_by_key(
            db,
            user_id,
            store_item_id
        )

        if not equipment:
            raise ValueError("Equipment not found")

        # Return quantity to store
        item = self.store_repository.get_by_id(
            db,
            equipment.store_item_id
        )

        if item:
            item.quantity += equipment.quantity

        self.repository.delete(
            db,
            equipment
        )

        return {
            "message": "Equipment deleted successfully"
        }

