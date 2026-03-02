from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
import logging

from src.infrastructure.config import settings
from src.infrastructure.api.v1.router import api_router

from src.domain.exceptions import AppError, ErrorCode
from src.infrastructure.api.v1.schemas.response import ErrorResponse, ErrorDetail

# Main instance
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    description="Backend for FlowMint using Hexagonal Architecture",
    version="0.1.0",
)

logger = logging.getLogger(__name__)

# --- GLOBAL HANDLERS ---

@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    """Captures our business errors and puts them in the {error, meta} envelope"""
    response_obj = ErrorResponse(
        error=ErrorDetail(
            code=exc.error_code.value,
            message=exc.message,
            details=exc.details
        )
    )
    return JSONResponse(
        status_code=exc.http_status,
        content=response_obj.model_dump(mode="json") # mode="json" serializa el timestamp
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """Captures Pydantic errors (e.g. the frontend sent a string instead of an int)"""
    response_obj = ErrorResponse(
        error=ErrorDetail(
            code=ErrorCode.VALIDATION_ERROR.value,
            message="Error in the validation of the sent data.",
            details=exc.errors()
        )
    )
    return JSONResponse(status_code=422, content=response_obj.model_dump(mode="json"))


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