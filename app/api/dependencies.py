from app.repositories.item_repository import ItemRepository
from app.repositories.category_repository import CategoryRepository

from app.services.item_service import ItemService
from app.services.category_service import CategoryService


def get_item_service() -> ItemService:
    repository = ItemRepository()

    return ItemService(
        repository
    )

def get_category_service() -> CategoryService:
    repository = CategoryRepository()

    return CategoryService(
        repository
    )