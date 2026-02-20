from datetime import datetime
from sqlalchemy import String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.persistence.db import Base

class TransactionModel(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    
    # From which allocation did the money come?
    allocation_id: Mapped[int] = mapped_column(ForeignKey("allocations.id", ondelete="CASCADE"), index=True)
    
    # Expense details
    amount: Mapped[int] = mapped_column(Integer, nullable=False) # Cents
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    transaction_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationship
    allocation: Mapped["AllocationModel"] = relationship("AllocationModel", back_populates="transactions")