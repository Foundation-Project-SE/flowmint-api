from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID

class AllocationBase(BaseModel):
    category_id: UUID = Field(..., description="ID of the category")
    period_id: UUID = Field(..., description="ID of the budget period")
    amount: int = Field(..., ge=0, description="Amount allocated in CENTS (e.g. 1000 = $10.00)")

class AllocationCreate(AllocationBase):
    pass

class AllocationResponse(AllocationBase):
    id: UUID

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "category_id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
                "period_id": "123e4567-e89b-12d3-a456-426614174000",
                "amount": 20000 # This is $200.00
            }
        }
    )