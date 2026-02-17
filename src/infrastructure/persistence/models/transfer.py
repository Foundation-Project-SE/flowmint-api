from datetime import datetime
from sqlalchemy import String, Integer, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.persistence.db import Base

class TransferModel(Base):
    __tablename__ = "transfers"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)

    # The originating allocation and the destination allocation
    from_allocation_id: Mapped[int] = mapped_column(ForeignKey("allocations.id", ondelete="CASCADE"), nullable=False)
    to_allocation_id: Mapped[int] = mapped_column(ForeignKey("allocations.id", ondelete="CASCADE"), nullable=False)

    # Money in Cents ** Might be refactored
    amount: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)

    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationships: 
    # there are two foreign keys pointing to the same table
    from_allocation: Mapped["AllocationModel"] = relationship(
        "AllocationModel", foreign_keys=[from_allocation_id]
    )
    to_allocation: Mapped["AllocationModel"] = relationship(
        "AllocationModel", foreign_keys=[to_allocation_id]
    )