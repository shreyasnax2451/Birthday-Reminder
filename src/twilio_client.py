import os
import logging

from twilio.rest import Client
# from env import ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER
ACCOUNT_SID = os.environ["ACCOUNT_SID"]
AUTH_TOKEN = os.environ["AUTH_TOKEN"]
FROM_NUMBER = os.environ["FROM_NUMBER"]
TO_NUMBER = os.environ["TO_NUMBER"]

logger = logging.getLogger(__name__)

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_message(birthday_date):
    try:
        message_body = birthday_date.notification_message
        message = client.messages.create(
            from_=f'whatsapp:{FROM_NUMBER}',  # This is Twilio's default WhatsApp sandbox number
            body=message_body,
            to=f'whatsapp:{TO_NUMBER}'
        )
        logger.info(f"Message sent successfully. SID: {message.sid}")
    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")
