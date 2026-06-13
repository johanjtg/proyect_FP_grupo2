from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.expense import CategoryEnum


class ExpenseCreate(BaseModel):
    amount: float
    category: CategoryEnum
    description: Optional[str] = None
    is_subscription: bool = False


class ExpenseResponse(ExpenseCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class AlertRuleCreate(BaseModel):
    category: Optional[CategoryEnum] = None
    threshold: float
    condition: str  # "gt" or "lt"


class AlertRuleResponse(AlertRuleCreate):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class CategorySummary(BaseModel):
    category: str
    total: float
    count: int
