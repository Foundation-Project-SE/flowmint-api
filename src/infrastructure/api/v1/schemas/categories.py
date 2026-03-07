from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Name of the category")
    is_income: bool = Field(default=False, description="True if this is an income source, False for expenses")
    icon: str | None = Field(default=None, description="Optional emoji or icon identifier")

class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: UUID

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
                "name": "Supermarket",
                "is_income": False,
                "icon": "🛒"
            }
        }
    )