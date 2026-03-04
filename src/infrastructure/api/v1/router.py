from fastapi import APIRouter
from src.infrastructure.api.v1.endpoints import (
    periods,
    categories,
    allocations,
    transactions,
    transfers,
    snapshot
)

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

# 1. Core Budgeting
api_router.include_router(periods.router, prefix="/periods", tags=["periods"])
api_router.include_router(categories.router, prefix="/categories", tags=["categories"])
api_router.include_router(allocations.router, prefix="/allocations", tags=["allocations"])

# 2. Money Movement
api_router.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
api_router.include_router(transfers.router, prefix="/transfers", tags=["transfers"])

# 3. Analytics/Views
api_router.include_router(snapshot.router, prefix="/snapshot", tags=["snapshot"])

