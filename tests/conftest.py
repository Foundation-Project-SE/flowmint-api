"""Pytest configuration and shared fixtures."""

import os

# Set default DATABASE_URL for tests if not set (required by Settings at import time).
os.environ.setdefault(
    "DATABASE_URL",
    "postgresql+asyncpg://user:pass@localhost:5432/testdb",
)
