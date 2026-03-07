"""Integration tests for /me endpoint."""

import pytest
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_me_without_authorization_returns_401() -> None:
    """When Authorization header is missing, returns 401."""
    response = client.get("/api/v1/me")
    assert response.status_code == 401
    assert "token" in response.json()["detail"].lower() or "authentication" in response.json()["detail"].lower()


def test_me_with_empty_bearer_returns_401() -> None:
    """When Authorization header has empty Bearer value, returns 401."""
    response = client.get(
        "/api/v1/me",
        headers={"Authorization": "Bearer "},
    )
    assert response.status_code == 401
