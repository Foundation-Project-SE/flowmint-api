from pydantic import BaseModel, Field, ConfigDict
from uuid import UUID
from datetime import datetime

class TransferBase(BaseModel):
    from_allocation_id: UUID = Field(..., description="Source allocation ID")
    to_allocation_id: UUID = Field(..., description="Destination allocation ID")
    amount: int = Field(..., gt=0, description="Amount to transfer in CENTS")
    description: str | None = Field(default=None, description="Reason for the transfer")

class TransferCreate(TransferBase):
    pass

class TransferResponse(TransferBase):
    id: UUID
    transfer_date: datetime

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
                "from_allocation_id": "550e8400-e29b-41d4-a716-446655440000",
                "to_allocation_id": "660e8400-e29b-41d4-a716-446655441111",
                "amount": 5000, # $50.00
                "description": "Moving leftover groceries money to savings",
                "transfer_date": "2026-03-25T10:00:00Z"
            }
        }
    )