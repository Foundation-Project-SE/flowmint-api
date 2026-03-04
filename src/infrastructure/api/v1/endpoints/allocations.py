from fastapi import APIRouter
from src.infrastructure.api.v1.schemas.allocations import AllocationResponse, AllocationCreate

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
    pass