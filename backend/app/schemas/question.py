from pydantic import BaseModel

class QuestionCreate(BaseModel):
    topic : str 
    difficulty : str 
    question_text : str

class QuestionResponse(BaseModel):
    id : int 
    topic : str 
    difficulty : str 
    question_text : str
    class Config:
        from_attributes=True