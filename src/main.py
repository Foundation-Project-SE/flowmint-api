from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from src.infrastructure.config import settings
from src.infrastructure.api.v1.router import api_router

# Main instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Backend for FlowMind using Hexagonal Architecture",
    version="0.1.0",
)

# --- CORS configuration ---
# if origins list has elements, middleware gets active
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"], # Allow all methods (GET, POST, PUT, DELETE)
        allow_headers=["*"], # Allow all headers (Authorization, etc.)
    )

# Main router v1 include
app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/", include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")