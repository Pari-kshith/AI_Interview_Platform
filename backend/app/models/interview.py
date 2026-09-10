from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database.base import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"),nullable=False)

    interview_type = Column(String(100), nullable=False)

    score = Column(Float)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship(
        "User",
        back_populates="interviews"
    )

    answers=relationship(
        "Answer",
        back_populates="interview",
        cascade="all, delete-orphan"
    )