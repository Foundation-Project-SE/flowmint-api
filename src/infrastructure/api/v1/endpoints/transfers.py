from datetime import datetime, timezone
from uuid import uuid4

from fastapi import APIRouter

from src.infrastructure.api.v1.schemas.transfers import TransferCreate, TransferResponse

router = APIRouter()


@router.get("/", response_model=list[TransferResponse])
async def get_transfers():
    """
    Retrieve all internal transfers.
    """
    return []


@router.post("/", response_model=TransferResponse, status_code=201)
async def create_transfer(transfer_in: TransferCreate):
    """
    Execute a fund transfer between allocations.
    """
    # Mock response until use case + repository are implemented. TODO: inject AuthContext and pass user_id.
    return TransferResponse(
        id=uuid4(),
        from_allocation_id=transfer_in.from_allocation_id,
        to_allocation_id=transfer_in.to_allocation_id,
        amount=transfer_in.amount,
        description=transfer_in.description,
        transfer_date=datetime.now(timezone.utc),
    )