from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)