from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine
from app.database.init_db import init_db

from app.api.auth import router as auth_router
from app.api.interview import router as interview_router
from app.api.question import app as question_router
from app.api.answer import router as answer_router
app = FastAPI(
    title="AI Interview Platform"
)


@app.on_event("startup")
def startup():

    init_db()

@app.get("/")
def home():

    return {
        "message": "AI Interview Platform Backend Running"
    }


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


app.include_router(auth_router)

app.include_router(interview_router)
app.include_router(question_router)
app.include_router(answer_router)