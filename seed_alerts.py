from app.database import SessionLocal, engine
from app.models.expense import Base, AlertRule, CategoryEnum

Base.metadata.create_all(bind=engine)

DEFAULT_RULES = [
    {"category": CategoryEnum.food,          "threshold": 300.0, "condition": "gt"},
    {"category": CategoryEnum.subscriptions, "threshold":  50.0, "condition": "gt"},
    {"category": CategoryEnum.transport,     "threshold": 150.0, "condition": "gt"},
    {"category": CategoryEnum.entertainment, "threshold": 100.0, "condition": "gt"},
    {"category": CategoryEnum.health,        "threshold": 200.0, "condition": "gt"},
    {"category": CategoryEnum.other,         "threshold": 100.0, "condition": "gt"},
]

db = SessionLocal()

existing = db.query(AlertRule).count()
if existing > 0:
    print(f"Ya existen {existing} reglas. No se insertan duplicados.")
else:
    for rule_data in DEFAULT_RULES:
        db.add(AlertRule(**rule_data))
    db.commit()
    print(f"{len(DEFAULT_RULES)} reglas de alerta insertadas correctamente.")

db.close()
