from operator import index
from sqlalchemy import JSON, Column, Integer, PrimaryKeyConstraint, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Chat(Base):
    __tablename__ = "chats"
    user = Column(String, nullable=False)
    title = Column(String, nullable=False)
    messages = Column(JSON, nullable=False)

    __table_args = (PrimaryKeyConstraint('user', 'title'))
