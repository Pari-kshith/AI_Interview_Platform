from sqlalchemy import Integer,Column,ForeignKey,DateTime,Text
from app.database.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Answer(Base):
    __tablename__="answers"
    id=Column(Integer,primary_key=True,index=True)

    question_id=Column(Integer,ForeignKey("questions.id"),nullable=False)

    interview_id=Column(Integer,ForeignKey("interviews.id"),nullable=False)

    answer_text=Column(Text,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

    interview=relationship(
        "Interview",
        back_populates="answers"
    )
    question=relationship(
        "Question",
        back_populates="answers"
    )


