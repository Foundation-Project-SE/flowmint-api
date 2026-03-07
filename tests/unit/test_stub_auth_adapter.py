"""Unit tests for StubAuthContextAdapter."""

import pytest

from src.application.ports.auth_context import AuthContext, AuthenticationError
from src.infrastructure.auth.stub_adapter import StubAuthContextAdapter
from src.infrastructure.config import settings


def test_valid_token_returns_auth_context(monkeypatch: pytest.MonkeyPatch) -> None:
    """When token matches configured token, returns AuthContext with user_id."""
    monkeypatch.setattr(settings, "is_stub_auth_enabled", lambda: True)
    monkeypatch.setattr(settings, "STUB_AUTH_TOKEN", "test-token-mvp")
    monkeypatch.setattr(settings, "STUB_AUTH_USER_ID", "123e4567-e89b-12d3-a456-426614174000")

    adapter = StubAuthContextAdapter()
    result = adapter.from_bearer_token("test-token-mvp")

    assert result == AuthContext(user_id="123e4567-e89b-12d3-a456-426614174000")


def test_invalid_token_raises_authentication_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """When token does not match, raises AuthenticationError."""
    monkeypatch.setattr(settings, "is_stub_auth_enabled", lambda: True)
    monkeypatch.setattr(settings, "STUB_AUTH_TOKEN", "valid-token")
    monkeypatch.setattr(settings, "STUB_AUTH_USER_ID", "user-123")

    adapter = StubAuthContextAdapter()

    with pytest.raises(AuthenticationError):
        adapter.from_bearer_token("wrong-token")


def test_stub_disabled_raises_authentication_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """When stub auth is disabled, raises AuthenticationError regardless of token."""
    monkeypatch.setattr(settings, "is_stub_auth_enabled", lambda: False)
    monkeypatch.setattr(settings, "STUB_AUTH_TOKEN", "test-token")
    monkeypatch.setattr(settings, "STUB_AUTH_USER_ID", "user-123")

    adapter = StubAuthContextAdapter()

    with pytest.raises(AuthenticationError):
        adapter.from_bearer_token("test-token")


def test_empty_token_raises_authentication_error(monkeypatch: pytest.MonkeyPatch) -> None:
    """When token is empty, raises AuthenticationError."""
    monkeypatch.setattr(settings, "is_stub_auth_enabled", lambda: True)
    monkeypatch.setattr(settings, "STUB_AUTH_TOKEN", "valid-token")
    monkeypatch.setattr(settings, "STUB_AUTH_USER_ID", "user-123")

    adapter = StubAuthContextAdapter()

    with pytest.raises(AuthenticationError):
        adapter.from_bearer_token("")


def test_empty_configured_token_rejects_all(monkeypatch: pytest.MonkeyPatch) -> None:
    """When STUB_AUTH_TOKEN is empty, rejects all tokens (no guessing)."""
    monkeypatch.setattr(settings, "is_stub_auth_enabled", lambda: True)
    monkeypatch.setattr(settings, "STUB_AUTH_TOKEN", "")
    monkeypatch.setattr(settings, "STUB_AUTH_USER_ID", "user-123")

    adapter = StubAuthContextAdapter()

    with pytest.raises(AuthenticationError):
        adapter.from_bearer_token("any-token")
