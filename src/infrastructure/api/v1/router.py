from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/health", tags=["System"])
async def health_check():
    """Verifica que el sistema esté operativo."""
    return {
        "status": "ok",
        "app": "FlowMint API",
        "version": "0.1.0"
    }

@api_router.get("/ping", tags=["System"])
async def ping():
    """Prueba de latencia simple."""
    return {"message": "pong"}
