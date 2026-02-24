from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from lib.db import get_db
from models.question import *
from schemas.questions import *

questionsRouter = APIRouter()

# get all questions
@questionsRouter.get(
    "/get/all",
    status_code=status.HTTP_200_OK,
    response_model= SaveQuestionListResponse
)
def get_all_questions(db: Session = Depends(get_db)):
    try:
        
        questions = db.execute(select(Question)).scalars().all()
        return {"items": questions}
    
    except SQLAlchemyError as sqla_e:
        print("SQLAlchemy Error:", sqla_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="SQLAlchemy Error"
        )

# get specific questions by id
@questionsRouter.get(
    "/get/{question_id}",
    status_code=status.HTTP_200_OK,
    response_model= SaveQuestionResponse
)
def get_question_by_id(question_id: int, db: Session = Depends(get_db)):
    try:
        question = db.get(Question, question_id)
        return question
    
    except SQLAlchemyError as sqla_e:
        print("SQLAlchemy Error:", sqla_e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="SQLAlchemy Error"
        )

# save questions to db(automatically happens after llm_call)
@questionsRouter.post(
    "/save",
    # response_model=,
    status_code=status.HTTP_201_CREATED
)
def save_question(payload: SaveQuestionRequest , db: Session = Depends(get_db)):
    try:
        dict_data = payload.model_dump()

        new_data = Question(
            questions=dict_data["questions"],
            topic=payload.metadata.topic,
            no_of_questions=payload.metadata.no_of_questions,
            llm_message=payload.metadata.message,
            total_marks=payload.metadata.total_marks,
            minimum_marks=payload.metadata.minimum_marks,
            marks_scored=0  # Initializing as 0 for now
        )

        db.add(new_data)
        db.commit()
        db.refresh(new_data)

        return new_data

    except SQLAlchemyError as sqla_e:
        db.rollback()
        print("SQLAlchemy Error:", sqla_e)

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="SQLAlchemy Error"
        )
    
