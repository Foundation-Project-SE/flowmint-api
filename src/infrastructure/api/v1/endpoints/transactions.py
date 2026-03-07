from uuid import uuid4

from fastapi import APIRouter

from src.infrastructure.api.v1.schemas.transactions import TransactionCreate, TransactionResponse

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
    # Mock response until use case + repository are implemented. TODO: inject AuthContext and pass user_id.
    return TransactionResponse(
        id=uuid4(),
        category_id=transaction_in.category_id,
        amount=transaction_in.amount,
        description=transaction_in.description,
        transaction_date=transaction_in.transaction_date,
    )