import streamlit as st
from datetime import datetime

from create_update_operations import create_user_birthday
from birthday_scheduler import schedule_notifications

st.title("Birthday Reminder")


name = st.text_input("Name of your Friend")
birthdate = st.date_input(
    label="Birthdate of your Friend",
    min_value=datetime(1980, 1, 1))
notification_message = f" {name} ki message cheyyi bhaiya birthday anta!"
notification_input = st.text_input("Any Special Notification that you want to get reminded!")
notification_message += notification_input


button = st.button("Add to the List!")
if button:
    user_birthday = create_user_birthday(
        name=name,
        birthdate=birthdate,
        notification_message=notification_message
    )
    if not user_birthday:
        st.error("Birthday Not Created!")
    else:
        schedule_notifications(user_birthday)
