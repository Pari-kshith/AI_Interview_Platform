from pydantic import BaseModel
from datetime import datetime

class AnswerCreate(BaseModel):
    interview_id : int 
    question_id : int 
    answer_text : str 

class AnswerResponse(BaseModel):
    id:int 
    interview_id : int 
    question_id : int 
    answer_text : str 
    created_at : datetime 

    class Config:
        from_attributes=True