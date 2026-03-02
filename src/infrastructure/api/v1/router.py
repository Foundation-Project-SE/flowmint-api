from fastapi import APIRouter, Depends
from src.infrastructure.auth.dependencies import get_current_user_id_stub

api_router = APIRouter()

@api_router.get("/health", tags=["System"])
async def health_check():
    """Check if system is currently operational."""
    return {
        "status": "ok",
        "app": "FlowMind API",
        "version": "0.1.0"
    }

@api_router.get("/ping", tags=["System"])
async def ping():
    """Simple latency check"""
    return {"message": "pong"}

@api_router.get("/me")
def get_my_profile(current_user_id: str = Depends(get_current_user_id_stub)):
    """
    This route is protected. FastAPI will inject the user ID
    only if the token is valid according to our Stub.
    """
    return {
        "message": "You have entered the VIP zone!",
        "user_id": current_user_id
    }