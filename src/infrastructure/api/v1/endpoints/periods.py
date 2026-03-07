from uuid import uuid4

from fastapi import APIRouter

from src.infrastructure.api.v1.schemas.periods import BudgetPeriodCreate, BudgetPeriodResponse

router = APIRouter()


@router.get("/", response_model=list[BudgetPeriodResponse])
async def get_periods():
    """
    Retrieve all budget periods.
    """
    return []  # Temporary empty response until we connect the Domain/DB


@router.post("/", response_model=BudgetPeriodResponse, status_code=201)
async def create_period(period_in: BudgetPeriodCreate):
    """
    Create a new budget period.
    """
    # Mock response until use case + repository are implemented. TODO: inject AuthContext and pass user_id.
    return BudgetPeriodResponse(
        id=uuid4(),
        start_date=period_in.start_date,
        end_date=period_in.end_date,
        name=period_in.name,
    )