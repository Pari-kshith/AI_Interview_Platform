from pydantic import BaseModel
from typing import Optional 
from datetime import datetime
class InterviewCreate(BaseModel):
    interview_type:str 

class InterviewResponse(BaseModel):
    id : int 
    user_id : int 
    interview_type : str 
    score : Optional[float]=None 
    created_at : Optional[datetime]=None 

    class Config:
        from_attributes=True