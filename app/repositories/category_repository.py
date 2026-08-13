from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database.models.category import Category
from app.schemas import CategoryCreate, CategoryUpdate


class CategoryRepository:

    def get_all(
            self,
            db: Session,
    ) -> list[Category]:

        statement = select(Category)

        return list(db.scalars(statement).all())

    def create(
            self,
            db: Session,
            category_data: CategoryCreate,
    ) -> Category:

        category = Category(
            name=category_data.name,
            description=category_data.description,
        )

        db.add(category)
        db.commit()
        db.refresh(category)

        return category

    def get_by_id(
            self,
            db: Session,
            category_id: int,
    ) -> Category | None:

        statement = select(Category).where(Category.id == category_id)

        return db.scalar(statement)

    def update(
            self,
            db: Session,
            category_id: int,
            category_data: CategoryUpdate,
    ) -> Category | None:

        category = self.get_by_id(
            db,
            category_id,
        )

        if category is None:
            return None

        update_data = category_data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(category, field, value)

        db.commit()
        db.refresh(category)

        return category

    def delete(
            self,
            db: Session,
            category_id: int,
    ) -> Category | None:

        category = self.get_by_id(
            db,
            category_id,
        )

        if category is None:
            return None

        db.delete(category)
        db.commit()

        return category