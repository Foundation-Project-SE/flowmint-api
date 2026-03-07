"""
Auth context port and models.

Defines the contract for authentication adapters.
No FastAPI or infrastructure dependencies.
"""

from dataclasses import dataclass
from typing import Protocol


class AuthenticationError(Exception):
    """Raised when authentication fails (invalid/expired token, missing credentials, etc.)."""

    pass


@dataclass(frozen=True)
class AuthContext:
    """Authenticated user context extracted from credentials."""

    user_id: str


class AuthContextPort(Protocol):
    """
    Port (interface) for authentication adapters.

    Implementations resolve a bearer token into an AuthContext.
    """

    def from_bearer_token(self, token: str) -> AuthContext:
        """
        Resolve a bearer token into an authenticated context.

        Args:
            token: The raw bearer token (e.g. JWT or magic token in stub).

        Returns:
            AuthContext with the authenticated user_id.

        Raises:
            AuthenticationError: If the token is invalid, expired, or rejected.
        """
        ...
