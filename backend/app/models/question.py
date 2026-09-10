from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.database.base import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)

    topic = Column(String(100), nullable=False)

    difficulty = Column(String(50), nullable=False)

    question_text = Column(Text, nullable=False)

    answers = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan"
    )