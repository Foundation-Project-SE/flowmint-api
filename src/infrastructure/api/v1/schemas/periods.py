from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from uuid import UUID

class BudgetPeriodBase(BaseModel):
    start_date: date = Field(..., description="Start date of the budget period")
    end_date: date = Field(..., description="End date of the budget period")
    name: str = Field(..., description="Name of the month/period (e.g., March 2026)")


# Create a new budget period, for now it is just the base model
class BudgetPeriodCreate(BudgetPeriodBase):
    pass

class BudgetPeriodResponse(BudgetPeriodBase):
    id: UUID

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "start_date": "2026-03-01",
                "end_date": "2026-03-31",
                "name": "March 2026"
            }
        }
    )