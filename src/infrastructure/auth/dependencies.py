"""
FastAPI dependencies for authentication.

Maps AuthContextPort to HTTP layer: extracts bearer token and converts
AuthenticationError to HTTP 401.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from src.application.ports.auth_context import AuthContext, AuthContextPort, AuthenticationError
from src.infrastructure.auth.stub_adapter import StubAuthContextAdapter

# Optional bearer: does not auto-raise when missing, so we can return custom 401.
security = HTTPBearer(auto_error=False)


def get_auth_adapter() -> AuthContextPort:
    """Provide the auth adapter implementation. Replace with Supabase adapter later."""
    return StubAuthContextAdapter()


def get_auth_context(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
    adapter: AuthContextPort = Depends(get_auth_adapter),
) -> AuthContext:
    """
    Extract AuthContext from the request.

    Requires Authorization: Bearer <token>.
    Maps AuthenticationError to HTTP 401.
    """
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication token missing",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        return adapter.from_bearer_token(credentials.credentials)
    except AuthenticationError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
