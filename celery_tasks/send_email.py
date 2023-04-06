import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import shared_task
from fastapi import Depends
from sqlalchemy.orm import Session

import models
from database import get_db
from settings import settings


def __send_email_message(msg):
    with smtplib.SMTP_SSL(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        server.login(settings.SMTP_EMAIL, settings.SMTP_PASSWORD)
        server.send_message(msg)


@shared_task
def send_verification_email(user,product_title) -> None:
    message = MIMEMultipart()
    message['Subject'] = 'Activation Code'
    message['From'] = settings.SMTP_EMAIL
    message['To'] = user.email
    html = f"""\
    <html>
      <body>
      <h1>
      Hi  
      </h1>
      <br>
      <h3>{product_title}</h3>
      </h2>
    </html> 
    """
    message.attach(MIMEText(html, 'html'))
    __send_email_message(message)
