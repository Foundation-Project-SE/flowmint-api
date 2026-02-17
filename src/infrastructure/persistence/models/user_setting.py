from datetime import datetime
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.persistence.db import Base

class UserSettingsModel(Base):
    __tablename__ = "user_settings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # constraint: one configuration row per user
    user_id: Mapped[str] = mapped_column(String(36), unique=True, index=True, nullable=False)

    # ISO format for currency (eg. 'USD', 'VES', 'EUR')
    base_currency: Mapped[str] = mapped_column(String(3), nullable=False, default="USD")
    
    # Audit
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())