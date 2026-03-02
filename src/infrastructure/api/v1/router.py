from fastapi import APIRouter

from src.domain.exceptions import AppError, ErrorCode
from src.infrastructure.api.v1.schemas.response import DataResponse

api_router = APIRouter()

@api_router.get("/health", response_model=DataResponse[dict])
def health_check():
    # Testing the success envelope
    return DataResponse(data={"status": "ok", "database": "connected"})

@api_router.get("/test-error")
def test_error():
    # Testing to throw a business error from anywhere
    raise AppError(
        error_code=ErrorCode.PERIOD_CLOSED,
        message="You cannot register transactions in a closed month."
    )

#@api_router.get("/health", tags=["System"])
#async def health_check():
#    """Check if system is currently operational."""
#    return {
#        "status": "ok",
#        "app": "FlowMind API",
#        "version": "0.1.0"
#    }

@api_router.get("/ping", tags=["System"])
async def ping():
    """Simple latency check"""
    return {"message": "pong"}
