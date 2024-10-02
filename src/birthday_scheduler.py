from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from datetime import datetime, timedelta
import streamlit as st

from twilio_client import send_whatsapp_message

from models import Birthday

scheduler = BackgroundScheduler(jobstores={'default': MemoryJobStore()}, executors={
            'default': ThreadPoolExecutor(), 'processpool': ProcessPoolExecutor()})

def schedule_notifications(birthday_object: Birthday) -> None:
    reminder_time = datetime(
        datetime.now().year,
        birthday_object.birthdate.month,
        birthday_object.birthdate.day,
        2,15,0)

    scheduler.add_job(
        send_whatsapp_message, "date", run_date=reminder_time, args=[birthday_object]
    )
    st.success("Birthday Created Successfully!")

scheduler.start()
