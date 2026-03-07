from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel, Field
from datetime import datetime, timezone

# Type variable to indicate that "Data" can be any model
T = TypeVar('T')

class Meta(BaseModel):
    """Metadata of the response"""
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ErrorDetail(BaseModel):
    """Standardized object error structure"""
    code: str
    message: str
    details: Optional[Any] = None

class DataResponse(BaseModel, Generic[T]):
    """Success response schema: { data: {...}, meta: {...} }"""
    data: T
    meta: Meta = Field(default_factory=Meta)

class ErrorResponse(BaseModel):
    """Failed response schema: { error: {...}, meta: {...} }"""
    error: ErrorDetail
    meta: Meta = Field(default_factory=Meta)