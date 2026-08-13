from sqlalchemy.orm import Session

from app.database.models.category import Category
from app.exceptions.category import CategoryNotFoundException
from app.repositories.category_repository import CategoryRepository
from app.schemas.category import CategoryCreate, CategoryUpdate

class CategoryService:
    def __init__(
            self, 
            repository: CategoryRepository,
    ):
        self.category_repository = repository

    def get_all(
            self,
            db: Session,
    ) -> list[Category]:

        return self.category_repository.get_all(db)

    def create(
            self,
            db: Session,
            category_data: CategoryCreate,
    ) -> Category:

        return self.category_repository.create(
            db,
            category_data,
        )

    def get_by_id(
            self,
            db: Session,
            category_id: int,
    ) -> Category:

        category = self.category_repository.get_by_id(
            db,
            category_id,
        )

        if category is None:
            raise CategoryNotFoundException(
                f"Category with id {category_id} not found"
            )

        return category

    def update(
            self,
            db: Session,
            category_id: int,
            category_data: CategoryUpdate,
    ) -> Category:

        category = self.category_repository.update(
            db,
            category_id,
            category_data,
        )

        if category is None:
            raise CategoryNotFoundException(
                f"Category with id {category_id} not found"
            )

        return category

    def delete(
            self,
            db: Session,
            category_id: int,
    ) -> None:

        category = self.category_repository.delete(
            db,
            category_id,
        )

        if category is None:
            raise CategoryNotFoundException(
                f"Category with id {category_id} not found"
            )

        return category