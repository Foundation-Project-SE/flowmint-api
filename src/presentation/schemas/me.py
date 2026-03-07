"""Response schemas for the /me endpoint."""

from pydantic import BaseModel


class MeResponse(BaseModel):
    """Authenticated user profile (minimal)."""

    message: str
    user_id: str
