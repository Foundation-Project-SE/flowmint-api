from fastapi import APIRouter
from src.infrastructure.api.v1.schemas.transfers import TransferResponse, TransferCreate

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
    pass