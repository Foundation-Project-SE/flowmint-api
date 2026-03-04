from fastapi import APIRouter
from src.infrastructure.api.v1.schemas.categories import CategoryResponse, CategoryCreate

router = APIRouter()

@router.get("/", response_model=list[CategoryResponse])
async def get_categories():
    """
    Retrieve all categories.
    """
    return []

@router.post("/", response_model=CategoryResponse, status_code=201)
async def create_category(category_in: CategoryCreate):
    """
    Create a new category.
    """
    pass