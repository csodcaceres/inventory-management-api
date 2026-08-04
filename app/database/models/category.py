from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.database.models.product import Product

class Category(BaseModel):
    """
    Category model representing a category entity in the database.
    Inherits from BaseModel to include common fields like id, created_at, and updated_at.
    """

    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False, 
        unique=True
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    products: Mapped[list["Product"]] = relationship(
        back_populates="category",
    )