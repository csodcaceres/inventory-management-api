from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.services.category_service import CategoryService
from app.api.dependencies import get_category_service

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)

@router.get(
    "/", 
    response_model=list[CategoryResponse], 
    status_code=status.HTTP_200_OK,)
def list_categories(
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_category_service),
):
    return service.get_all(db)

@router.post(
    "/", 
    response_model=CategoryResponse, 
    status_code=status.HTTP_201_CREATED,)
def create_category(
    category_data: CategoryCreate,
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_category_service),
):
    return service.create(
        db,
        category_data,
    )

@router.get(
    "/{category_id}", 
    response_model=CategoryResponse, 
    status_code=status.HTTP_200_OK,)
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_category_service),
):
    return service.get_by_id(
        db,
        category_id,
    )

@router.put(
    "/{category_id}", 
    response_model=CategoryResponse, 
    status_code=status.HTTP_200_OK,)
def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_category_service),
):
    return service.update(
        db,
        category_id,
        category_data,
    )

@router.delete(
    "/{category_id}", 
    response_model=CategoryResponse, 
    status_code=status.HTTP_200_OK,)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
    service: CategoryService = Depends(get_category_service),
):
    return service.delete(
        db,
        category_id,
    )