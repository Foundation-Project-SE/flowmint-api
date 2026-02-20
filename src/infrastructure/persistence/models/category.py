from datetime import datetime
from sqlalchemy import String, UniqueConstraint, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.persistence.db import Base

class CategoryModel(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(36), index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    
    # 'income' or 'expense'
    type: Mapped[str] = mapped_column(String(20), nullable=False, default="expense")

    # Audit 
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    # Inverse relationship: A category can have many envelopes (allocations) throughout the months
    allocations: Mapped[list["AllocationModel"]] = relationship("AllocationModel", back_populates="category", cascade="all, delete-orphan")

    __table_args__ = (
        # Constraint: Users can't have duplicate categories (same exact name)
        UniqueConstraint('user_id', 'name', name='uq_user_category_name'),
    )