from fastapi import APIRouter
from uuid import UUID
from src.infrastructure.api.v1.schemas.snapshot import PeriodSnapshot

router = APIRouter()


@router.get("/{period_id}", response_model=PeriodSnapshot)
async def get_period_snapshot(period_id: UUID):
    """
    Get the financial snapshot (summary) for a specific budget period.
    """
    # Mock response
    return PeriodSnapshot(
        period_id=period_id,
        total_income=0,
        total_allocated=0,
        total_spent=0,
        unallocated_balance=0,
    )
