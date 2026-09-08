from fastapi import APIRouter,Depends,status,HTTPException
from app.database.connection import get_db
from sqlalchemy.orm import Session
from app.models.question import Question
from app.schemas.question import QuestionCreate,QuestionResponse
app=APIRouter(
    prefix="/questions",
    tags=["Question"]
)

@app.get('',response_model=list[QuestionResponse])
def get_questions(topic:str |None=None, difficulty:str |None=None,db: Session=Depends(get_db)):
    query = db.query(Question)
    if topic:
        query=query.filter(Question.topic==topic)
    if difficulty:
        query=query.filter(Question.difficulty==difficulty)
    questions=query.all()
    return questions


@app.post("",status_code=status.HTTP_201_CREATED,response_model=QuestionResponse)
def create_question(question:QuestionCreate,db:Session=Depends(get_db)):
    new_question=Question(
        topic=question.topic,
        difficulty=question.difficulty,
        question_text=question.question_text
    )

    db.add(new_question)
    db.commit()
    db.refresh(new_question)

    return new_question

@app.get("/{question_id}",response_model=QuestionResponse)
def get_question(question_id : int,db:Session=Depends(get_db)):
    question=db.query(Question).filter(Question.id==question_id).first()

    if question is None:
        raise HTTPException(status_code=404,
                            detail="Question Not Found")

    return question