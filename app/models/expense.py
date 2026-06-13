from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Enum
from sqlalchemy.sql import func
from app.database import Base
import enum


class CategoryEnum(str, enum.Enum):
    food = "Food"
    subscriptions = "Subscriptions"
    transport = "Transport"
    entertainment = "Entertainment"
    health = "Health"
    other = "Other"


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    description = Column(String, nullable=True)
    is_subscription = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class AlertRule(Base):
    __tablename__ = "alert_rules"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(Enum(CategoryEnum), nullable=True)  # None = applies to all
    threshold = Column(Float, nullable=False)
    condition = Column(String, nullable=False)  # "gt" or "lt"
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
