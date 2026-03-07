from fastapi import APIRouter

from src.domain.exceptions import AppError, ErrorCode
from src.infrastructure.api.v1.schemas.response import DataResponse

api_router = APIRouter()


@api_router.get("/health", response_model=DataResponse[dict], tags=["System"])
async def health_check():
    """Check if system is currently operational. Returns success envelope."""
    return DataResponse(data={"status": "ok", "database": "connected"})


@api_router.get("/test-error", tags=["System"])
async def test_error():
    """Demonstrates business error envelope (PERIOD_CLOSED). Remove or guard in production."""
    raise AppError(
        error_code=ErrorCode.PERIOD_CLOSED,
        message="You cannot register transactions in a closed month.",
    )


@api_router.get("/ping", response_model=DataResponse[dict], tags=["System"])
async def ping():
    """Simple latency check. Returns success envelope."""
    return DataResponse(data={"message": "pong"})
