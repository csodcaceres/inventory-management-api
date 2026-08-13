from app.exceptions.exceptions import NotFoundException

class CategoryNotFoundException(NotFoundException):
    """
    Exception raised when a category is not found.
    """
    pass