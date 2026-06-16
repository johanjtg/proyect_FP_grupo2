from fastapi import FastAPI
from app.database import Base, engine
from app.routes import expenses, alerts

Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI(title="Expense Tracker", version="0.1.0", redirect_slashes=False)

app.include_router(expenses.router)
app.include_router(alerts.router)


@app.get("/")
def root():
    return {"message": "Expense Tracker API is running"}
