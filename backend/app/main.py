from fastapi import FastAPI
from sqlalchemy import text
from app.database.init_db import init_db
from app.database.connection import engine
app = FastAPI(title="AI Interview Platform")

@app.on_event("startup")
def startup():
    init_db()


@app.get("/")
def home():
    return {"message": "AI Interview Platform Backend Running "}


@app.get("/health")
def health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "Database Connected"
        }

    except Exception as e:
        return {
            "status": "Database Not Connected",
            "error": str(e)
        }