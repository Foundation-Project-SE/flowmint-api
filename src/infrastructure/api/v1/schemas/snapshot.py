from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID


class PeriodSnapshot(BaseModel):
    period_id: UUID
    total_income: int = Field(..., description="Total income in CENTS")
    total_allocated: int = Field(
        ..., description="Total money assigned to envelopes in CENTS"
    )
    total_spent: int = Field(..., description="Total expenses in CENTS")
    unallocated_balance: int = Field(
        ..., description="Money left to be assigned (Income - Allocated)"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "period_id": "123e4567-e89b-12d3-a456-426614174000",
                "total_income": 300000,  # $3,000.00
                "total_allocated": 250000,  # $2,500.00
                "total_spent": 120000,  # $1,200.00
                "unallocated_balance": 50000,  # $500.00
            }
        }
    )
