from sqlalchemy.orm import Session

from app.modules.store.model import Store
from app.modules.store.repository import StoreRepository
from app.modules.store.schema import (
    StoreCreate,
    StoreUpdate,
)


class StoreService:

    def __init__(self):
        self.repository = StoreRepository()

    # =========================
    # Create Item
    # =========================

    def create_item(
        self,
        db: Session,
        item_data: StoreCreate
    ):
        # Check duplicate item Id
        if self.repository.get_by_id(db, item_data.id):
          
            raise ValueError("Store ID already exists")
        # Check duplicate item name
        if self.repository.get_by_name(
            db,
            item_data.item_name
        ):
            raise ValueError("Item already exists")

        new_item = Store(
        id=item_data.id,
        item_name=item_data.item_name,
        quantity=item_data.quantity,
        unit_value=item_data.unit_value,
        status=item_data.status
        
        )

        return self.repository.create(
            db,
            new_item
        )

    # =========================
    # Get All Items
    # =========================

    def get_all_items(
        self,
        db: Session
    ):
        return self.repository.get_all(db)

    # =========================
    # Get Item By ID
    # =========================

    def get_item_by_id(
        self,
        db: Session,
        item_id: int
    ):

        item = self.repository.get_by_id(
            db,
            item_id
        )

        if not item:
            raise ValueError("Item not found")

        return item

    # =========================
    # Update Item
    # =========================

    def update_item(
        self,
        db: Session,
        item_id: int,
        item_data: StoreUpdate
    ):

        item = self.repository.get_by_id(
            db,
            item_id
        )

        if not item:
            raise ValueError("Item not found")

        update_data = item_data.model_dump(
            exclude_unset=True
        )

        # Check duplicate item name
        if (
            "item_name" in update_data
            and update_data["item_name"] != item.item_name
        ):

            existing = self.repository.get_by_name(
                db,
                update_data["item_name"]
            )

            if existing:
                raise ValueError("Item already exists")

        for field, value in update_data.items():
            setattr(item, field, value)

        return self.repository.update(
            db,
            item
        )

    # =========================
    # Delete Item
    # =========================

    def delete_item(
        self,
        db: Session,
        item_id: int
    ):

        item = self.repository.get_by_id(
            db,
            item_id
        )

        if not item:
            raise ValueError("Item not found")

        self.repository.delete(
            db,
            item
        )

        return {
            "message": "Item deleted successfully"
        }