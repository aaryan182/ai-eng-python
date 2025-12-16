import smtplib
from email.message import EmailMessage

def send_email(to: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = "agent@example.com"
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP("localhost") as server:
        server.send_message(msg)

    return "Email sent successfully"