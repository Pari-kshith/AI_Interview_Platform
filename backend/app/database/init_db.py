from app.database.base import Base 
from app.database.connection import engine 
from app.models.user import User 
from app.models.question import Question 
from app.models.interview import Interview 

def init_db():
    Base.metadata.create_all(bind=engine)