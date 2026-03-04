from fastapi import APIRouter
from src.infrastructure.api.v1.schemas.periods import BudgetPeriodResponse, BudgetPeriodCreate

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
    pass  # Temporary placeholder