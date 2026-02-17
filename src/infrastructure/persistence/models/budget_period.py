from datetime import datetime
from sqlalchemy import String, UniqueConstraint, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

# Import base previously created.
from src.infrastructure.persistence.db import Base

class BudgetPeriodModel(Base):
    """
    Persistence Model for Budget Periods (e.g., '2026-02').
    Note: added the 'Model' suffix to differentiate it from the future Domain entity.
    """
    __tablename__ = "budget_periods"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # user_id: String because Supabase Auth generates UUIDs in text format.
    # index=True fast response on user searchs.
    user_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    
    # period_key: month storage on format YYYY-MM (Ej: "2026-02")
    period_key: Mapped[str] = mapped_column(String(7), nullable=False)
    
    # Auditing (creation date / modification date) 
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())    # Function delegated to Postgres
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Constraints
    # Users can't have duplicate periods"
    __table_args__ = (
        UniqueConstraint('user_id', 'period_key', name='uq_user_period'),
    )