from datetime import datetime
from sqlalchemy import Integer, ForeignKey, UniqueConstraint, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.persistence.db import Base

class AllocationModel(Base):
    __tablename__ = "allocations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # Foreign Keys
    period_id: Mapped[int] = mapped_column(ForeignKey("budget_periods.id", ondelete="CASCADE"), index=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete="CASCADE"), index=True)
    
    # Money in cents (Integer) *** Might be refactored
    budgeted_amount: Mapped[int] = mapped_column(Integer, default=0)    # Asigned by user
    available_amount: Mapped[int] = mapped_column(Integer, default=0)   # Available (asigned - expenses)
    
    # Audit
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Bidirectional relationships 
    category: Mapped["CategoryModel"] = relationship("CategoryModel", back_populates="allocations")
    transactions: Mapped[list["TransactionModel"]] = relationship("TransactionModel", back_populates="allocation")

    __table_args__ = (
        # Constraint: Can't duplicate categories on the same month ("February 2026")
        UniqueConstraint('period_id', 'category_id', name='uq_period_category'),
    )