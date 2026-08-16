from sqlalchemy.orm import Session

from app.modules.store.model import Store


class StoreRepository:

    # =========================
    # Create
    # =========================

    def create(
        self,
        db: Session,
        item: Store
    ):
        db.add(item)
        db.commit()
        db.refresh(item)

        return item

    # =========================
    # Get By ID
    # =========================

    def get_by_id(
        self,
        db: Session,
        item_id: int
    ):
      return (
        db.query(Store)
        .filter(Store.id == item_id)
        .first()
    )

    # =========================
    # Get By Name
    # =========================

    def get_by_name(
        self,
        db: Session,
        item_name: str
    ):
        return (
            db.query(Store)
            .filter(Store.item_name == item_name)
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
            db.query(Store)
            .all()
        )

    # =========================
    # Update
    # =========================

    def update(
        self,
        db: Session,
        item: Store
    ):
        db.commit()
        db.refresh(item)

        return item

    # =========================
    # Delete
    # =========================

    def delete(
        self,
        db: Session,
        item: Store
    ):
        db.delete(item)
        db.commit()