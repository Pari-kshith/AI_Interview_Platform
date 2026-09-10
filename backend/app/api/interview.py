from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User
from app.models.interview import Interview

from app.schemas.interview import (
    InterviewCreate,
    InterviewResponse
)

from app.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/interviews",
    tags=["Interviews"]
)


@router.post(
    "",
    response_model=InterviewResponse,
    status_code=status.HTTP_201_CREATED
)
def create_interview(
    interview_data: InterviewCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    new_interview = Interview(
        user_id=current_user.id,
        interview_type=interview_data.interview_type
    )

    db.add(new_interview)
    db.commit()
    db.refresh(new_interview)

    return new_interview

@router.get(
    "",
    response_model=list[InterviewResponse]
)
def get_interviews(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    interviews = db.query(Interview).filter(
        Interview.user_id == current_user.id
    ).all()

    return interviews


@router.get(
    "/{interview_id}",
    response_model=InterviewResponse
)
def get_interview(
    interview_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    interview = db.query(Interview).filter(
        Interview.id == interview_id,
        Interview.user_id == current_user.id
    ).first()

    if interview is None:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found"
        )

    return interview