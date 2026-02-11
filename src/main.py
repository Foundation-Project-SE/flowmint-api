from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from src.infrastructure.config import settings
from src.infrastructure.api.v1.router import api_router

# Main instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Backend for FlowMind using Hexagonal Architecture",
    version="0.1.0",
)

# Main router v1 include
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")