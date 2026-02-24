from sqlalchemy import Column, Integer, JSON, String

from lib.db import Base

class Question(Base):

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    questions = Column(JSON, nullable=False)
    topic = Column(String(100), nullable=False) #metadata
    no_of_questions = Column(Integer, nullable=False) #metadata
    llm_message = Column(String(200), nullable=True) #metadata
    total_marks = Column(Integer, nullable=False) #metadata
    minimum_marks = Column(Integer, nullable=False) #metadata
    marks_scored= Column(Integer, nullable=False)
