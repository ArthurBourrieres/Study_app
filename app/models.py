from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from .database import Base


class Exercise(Base):
    __tablename__ = 'exercise'
    id = Column(Integer, primary_key=True)
    subject = Column(String(50))
    chapter = Column(String(50))
    number = Column(String(50))
    status = Column(String(20))
    next_review_at = Column(DateTime)