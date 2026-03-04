from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from datetime import datetime

class TransactionBase(BaseModel):
    category_id: UUID = Field(..., description="ID of the category")
    amount: int = Field(..., description="Amount in CENTS (positive integer). E.g. 1500 = $15.00")
    description: str = Field(..., max_length=255, description="Description of the transaction")
    transaction_date: datetime = Field(default_factory=datetime.now, description="Date and time of the transaction")

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: UUID

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
                "category_id": "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11",
                "amount": 4500, # $45.00
                "description": "Lunch with team",
                "transaction_date": "2026-03-04T12:30:00Z"
            }
        }
    )