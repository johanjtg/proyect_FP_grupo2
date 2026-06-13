from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.expense import AlertRuleCreate, AlertRuleResponse

router = APIRouter(prefix="/alerts", tags=["Alerts"])


@router.post("/rules", response_model=AlertRuleResponse)
def create_alert_rule(rule: AlertRuleCreate, db: Session = Depends(get_db)):
    # TODO: implement — save alert rule
    pass


@router.get("/rules", response_model=List[AlertRuleResponse])
def list_alert_rules(db: Session = Depends(get_db)):
    # TODO: implement — return all active rules
    pass
