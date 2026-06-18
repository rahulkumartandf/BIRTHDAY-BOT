import smtplib
from email.message import EmailMessage

from messaging.base import MessageProvider


class EmailProvider(MessageProvider):

    def __init__(self, config):

        self.config = config

    def send(self, recipient, message):

        email = EmailMessage()

        email["Subject"] = "Happy Birthday"

        email["From"] = self.config["from"]

        email["To"] = recipient

        email.set_content(message)

        with smtplib.SMTP(
                self.config["host"],
                self.config["port"]
        ) as smtp:

            smtp.starttls()

            smtp.login(
                self.config["username"],
                self.config["password"]
            )

            smtp.send_message(email)