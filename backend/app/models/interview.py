from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.sql import func

from app.database.base import Base


class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    interview_type = Column(String(100), nullable=False)

    score = Column(Float)

    created_at = Column(DateTime(timezone=True), server_default=func.now())