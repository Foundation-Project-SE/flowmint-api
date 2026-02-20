from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.db import Base

class IdempotencyKeyModel(Base):
    __tablename__ = "idempotency_keys"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # Client generated key (Frontend)
    idempotency_key: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    
    user_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    
    # API route requested (Audit purposes, ej: "/api/v1/transactions")
    request_path: Mapped[str] = mapped_column(String(255), nullable=False)

    # Audit
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())