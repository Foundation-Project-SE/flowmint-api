"""
Stub implementation of AuthContextPort for MVP development.

Accepts a configured token and returns a configured user_id.
Disabled in production (APP_ENV=prod) or when STUB_AUTH_ENABLED=false.
"""

from src.application.ports.auth_context import AuthContext, AuthenticationError
from src.infrastructure.config import settings


class StubAuthContextAdapter:
    """
    Stub adapter that implements AuthContextPort.

    Reads STUB_AUTH_TOKEN and STUB_AUTH_USER_ID from config.
    If STUB_AUTH_TOKEN is empty, rejects all tokens (avoids guessing).
    """

    def from_bearer_token(self, token: str) -> AuthContext:
        if not settings.is_stub_auth_enabled():
            raise AuthenticationError("Stub auth is disabled")

        if not settings.STUB_AUTH_TOKEN:
            raise AuthenticationError("Stub auth token not configured")

        if not token:
            raise AuthenticationError("Token is required")

        if token != settings.STUB_AUTH_TOKEN:
            raise AuthenticationError("Invalid or expired token")

        if not settings.STUB_AUTH_USER_ID:
            raise AuthenticationError("Stub auth user_id not configured")

        return AuthContext(user_id=settings.STUB_AUTH_USER_ID)
