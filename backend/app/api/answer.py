from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm import Session 
from app.database.connection import get_db 
from app.models.answer import Answer 
from app.models.interview import Interview
from app. models.question import Question 
from app.models.user import User 

from app.schemas.answer import AnswerCreate,AnswerResponse 
from app.auth.dependencies import get_current_user

router=APIRouter(prefix="/answers",tags=["Answers"])

@router.post('',response_model=AnswerResponse,status_code=status.HTTP_201_CREATED)
def submit_answers(answer_data : AnswerCreate,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    interview=db.query(Interview).filter(Interview.id==answer_data.interview_id,Interview.user_id==current_user.id).first()
    if interview is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )

    question=db.query(Question).filter(Question.id==answer_data.question_id).first()
    if question is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Question not found"
        )

    new_answer=Answer(interview_id=answer_data.interview_id,question_id=answer_data.question_id,answer_text=answer_data.answer_text)

    db.add(new_answer)
    db.commit()
    db.refresh(new_answer)

    return new_answer


@router.get("/interview/{interview_id}",response_model=list[AnswerResponse])
def get_answers(interview_id : int,current_user:User=Depends(get_current_user),db:Session=Depends(get_db)):
    interview=db.query(Interview).filter(Interview.id==interview_id,Interview.user_id==current_user.id).first()
    if interview is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview Not Found"
        )

    answers=db.query(Answer).filter(Answer.interview_id==interview_id).all()

    return answers