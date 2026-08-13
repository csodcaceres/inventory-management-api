from pydantic import BaseModel, ConfigDict, Field

class CategoryBase(BaseModel):
    """ Base schema for Category model. """

    name: str = Field(
        ..., 
        min_length=2, 
        max_length=100,
    )

    description: str = Field(
        default=None, 
        max_length=255,
    )


class CategoryCreate(CategoryBase):
    """ Schema for creating a new Category. Inherits from CategoryBase. """
    pass


class CategoryUpdate(BaseModel):
    """ Schema for updating an existing Category. """
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100,
    )

    description: str | None = Field(
        default=None,
        max_length=255,
    )

class CategoryResponse(CategoryBase):
    """ Schema for returning Category data in responses. Inherits from CategoryBase. """

    id: int

    model_config = ConfigDict(from_attributes=True)

