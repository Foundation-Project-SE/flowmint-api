from uuid import uuid4

from fastapi import APIRouter

from src.infrastructure.api.v1.schemas.allocations import AllocationCreate, AllocationResponse

router = APIRouter()


@router.get("/", response_model=list[AllocationResponse])
async def get_allocations():
    """
    Retrieve all budget allocations for a specific period.
    """
    return []


@router.post("/", response_model=AllocationResponse, status_code=201)
async def create_allocation(allocation_in: AllocationCreate):
    """
    Create a new budget allocation.
    """
    # Mock response until use case + repository are implemented. TODO: inject AuthContext and pass user_id.
    return AllocationResponse(
        id=uuid4(),
        category_id=allocation_in.category_id,
        period_id=allocation_in.period_id,
        amount=allocation_in.amount,
    )