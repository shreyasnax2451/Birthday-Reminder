from sqlalchemy.orm import Session, sessionmaker, declarative_base
import streamlit as st

from datetime import datetime

from models import Birthday, engine

Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base()

def create_user_birthday(name: str, birthdate: str, notification_message: str) -> Birthday:
    existing_birthday = db_session.query(Birthday).filter(Birthday.name == name).first()
    if existing_birthday:
        st.warning("Birthday already exists, kindly edit!")
        return

    user_birthday = Birthday(
        name=name, 
        birthdate=birthdate,
        notification_message=notification_message,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    db_session.add(user_birthday)
    db_session.commit()
    db_session.refresh(user_birthday)
    return user_birthday

def update_user_birthday(*kwargs) -> Birthday:
    user_object = db_session.query(Birthday).filter(Birthday.id == kwargs["user_id"]).first()
    if user_object:
        user_object.name = kwargs["name"]
        user_object.birthdate = kwargs["birthdate"]
        user_object.notification_message = kwargs["notification_message"]
        db_session.commit()
        db_session.refresh(user_object)
    return user_object

def list_upcoming_birthdays():
    pass