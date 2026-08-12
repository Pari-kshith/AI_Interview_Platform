from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine
from app.database.init_db import init_db

from app.api.auth import router as auth_router


app = FastAPI(
    title="AI Interview Platform"
)


# -------------------------
# DATABASE STARTUP
# -------------------------

@app.on_event("startup")
def startup():

    init_db()


# -------------------------
# HOME
# -------------------------

@app.get("/")
def home():

    return {
        "message": "AI Interview Platform Backend Running"
    }


# -------------------------
# HEALTH CHECK
# -------------------------

@app.get("/health")
def health_check():

    try:

        with engine.connect() as connection:

            connection.execute(
                text("SELECT 1")
            )

        return {
            "status": "Database Connected"
        }

    except Exception as e:

        return {
            "status": "Database Not Connected",
            "error": str(e)
        }


# -------------------------
# AUTH ROUTES
# -------------------------

app.include_router(auth_router)