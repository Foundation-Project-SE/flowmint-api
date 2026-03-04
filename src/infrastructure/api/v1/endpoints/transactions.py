from fastapi import APIRouter
from src.infrastructure.api.v1.schemas.transactions import TransactionResponse, TransactionCreate

router = APIRouter()

@router.get("/", response_model=list[TransactionResponse])
async def get_transactions():
    """
    Retrieve all transactions (optionally filtered by period or category).
    """
    return []

@router.post("/", response_model=TransactionResponse, status_code=201)
async def create_transaction(transaction_in: TransactionCreate):
    """
    Log a new transaction.
    """
    pass