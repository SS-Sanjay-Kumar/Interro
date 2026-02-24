from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from lib.db import get_db
from models.question import *
from schemas.questions import *

def save_question_service(payload: SaveQuestionRequest , db: Session):

    dict_data = payload.model_dump()

    new_data = Question(
        questions=dict_data["questions"],
        topic=payload.metadata.topic,
        no_of_questions=payload.metadata.no_of_questions,
        llm_message = payload.metadata.message,
        total_marks=payload.metadata.total_marks,
        minimum_marks=payload.metadata.minimum_marks,
        marks_scored=0  # Initializing as 0 for now
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data