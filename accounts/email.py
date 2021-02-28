import smtplib, ssl
import os
from dotenv import load_dotenv
load_dotenv()


def send_notification(receiver_email, body):
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    message = f'From: {sender_email}\nTo: {receiver_email}\nSubject: Image uploaded!\n\n{body}'
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
