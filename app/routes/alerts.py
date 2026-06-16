from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.expense import AlertRule
from app.schemas.expense import AlertRuleCreate, AlertRuleResponse

router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.post("/rules", response_model=AlertRuleResponse, status_code=201)
def create_alert_rule(rule: AlertRuleCreate, db: Session = Depends(get_db)):
    if rule.condition not in ("gt", "lt"):
        raise HTTPException(status_code=422, detail="condition debe ser 'gt' o 'lt'")
    db_rule = AlertRule(**rule.model_dump())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule


@router.get("/rules", response_model=List[AlertRuleResponse])
def list_alert_rules(db: Session = Depends(get_db)):
    return db.query(AlertRule).filter(AlertRule.is_active == True).all()
