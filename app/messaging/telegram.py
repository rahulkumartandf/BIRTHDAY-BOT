from abc import abstractmethod

import requests
from messaging.base import MessageProvider


class TelegramProvider(MessageProvider):

    def __init__(self, token, chat_id):

        self.token = token
        self.chat_id = chat_id

    @abstractmethod
    def send(self, recipient, message):

        url = f"https://api.telegram.org/bot{self.token}/sendMessage"

        requests.post(url, json={
            "chat_id": self.chat_id,
            "text": message
        })