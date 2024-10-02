import os

from sqlalchemy import create_engine, DateTime, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir, "birthdays.db")
engine = create_engine(f"sqlite:///{db_path}", echo=True)

Base = declarative_base()

class Birthday(Base):
    __tablename__ = "birthdays"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, index=True)
    birthdate = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    notification_message = Column(String, unique=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
