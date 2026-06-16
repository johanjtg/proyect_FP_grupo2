from fastapi import APIRouter, Depends, Query
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Optional
from app.database import get_db
from app.models.expense import Expense, CategoryEnum
from app.schemas.expense import ExpenseCreate, ExpenseResponse, CategorySummary

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post("", response_model=ExpenseResponse, status_code=201)
@router.post("/", response_model=ExpenseResponse, status_code=201, include_in_schema=False)
def create_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = Expense(**expense.model_dump())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


@router.get("/", response_model=List[ExpenseResponse])
def list_expenses(
    category: Optional[CategoryEnum] = Query(default=None),
    is_subscription: Optional[bool] = Query(default=None),
    db: Session = Depends(get_db),
):
    query = db.query(Expense)
    if category:
        query = query.filter(Expense.category == category)
    if is_subscription is not None:
        query = query.filter(Expense.is_subscription == is_subscription)
    return query.order_by(Expense.created_at.desc()).all()


@router.get("/summary", response_model=List[CategorySummary])
def get_summary(db: Session = Depends(get_db)):
    results = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total"),
            func.count(Expense.id).label("count"),
        )
        .group_by(Expense.category)
        .all()
    )
    return [{"category": r.category, "total": r.total, "count": r.count} for r in results]
