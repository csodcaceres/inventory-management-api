from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.models.base_model import BaseModel

if TYPE_CHECKING:
    from app.database.models.category import Category

class Product(BaseModel):
    """
    Product model representing a product entity in the database.
    Inherits from BaseModel to include common fields like id, created_at, and updated_at.
    """

    __tablename__ = "products"

    name: Mapped[str] = mapped_column(
        String(100), 
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True
    )

    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2), 
        nullable=False
    )

    stock: Mapped[int] = mapped_column(
        nullable=False,
        default=0
    )

    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id"), 
        nullable=False
    )

    category: Mapped["Category"] = relationship(
        back_populates="products"
    )