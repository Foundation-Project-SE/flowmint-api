from uuid import uuid4

from fastapi import APIRouter

from src.infrastructure.api.v1.schemas.categories import CategoryCreate, CategoryResponse

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
    # Mock response until use case + repository are implemented. TODO: inject AuthContext and pass user_id.
    return CategoryResponse(
        id=uuid4(),
        name=category_in.name,
        is_income=category_in.is_income,
        icon=category_in.icon,
    )