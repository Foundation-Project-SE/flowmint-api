from fastapi import APIRouter, Depends

from src.application.ports.auth_context import AuthContext
from src.infrastructure.auth import get_auth_context
from src.presentation.schemas.me import MeResponse

api_router = APIRouter()


@api_router.get("/health", tags=["System"])
async def health_check():
    """Check if system is currently operational."""
    return {
        "status": "ok",
        "app": "FlowMind API",
        "version": "0.1.0",
    }


@api_router.get("/ping", tags=["System"])
async def ping():
    """Simple latency check."""
    return {"message": "pong"}


@api_router.get("/me", response_model=MeResponse)
async def get_my_profile(auth: AuthContext = Depends(get_auth_context)):
    """
    Protected route. Returns the authenticated user context.
    Requires valid Bearer token.
    """
    return MeResponse(
        message="You have entered the VIP zone!",
        user_id=auth.user_id,
    )