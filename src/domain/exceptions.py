from enum import Enum
from typing import Optional

class ErrorCode(str, Enum):
    """Official error catalog of the API (FlowMint MVP)"""
    # General
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    VALIDATION_ERROR = "VALIDATION_ERROR"
    UNAUTHORIZED = "UNAUTHORIZED"
    NOT_FOUND = "NOT_FOUND"
    
    # Business rules (Domain)
    PERIOD_CLOSED = "PERIOD_CLOSED"
    PARSE_AMOUNT_FAILED = "PARSE_AMOUNT_FAILED"
    INSUFFICIENT_FUNDS = "INSUFFICIENT_FUNDS"
    ENVELOPE_NOT_FOUND = "ENVELOPE_NOT_FOUND"

class AppError(Exception):
    """
    Base exception for the entire application.
    Any business rule that fails must raise this exception.
    """
    def __init__(
        self, 
        error_code: ErrorCode, 
        message: str, 
        http_status: int = 400,
        details: Optional[dict] = None
    ):
        self.error_code = error_code
        self.message = message
        self.http_status = http_status
        self.details = details
        super().__init__(self.message)