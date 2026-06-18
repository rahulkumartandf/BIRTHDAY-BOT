from abc import ABC, abstractmethod


class MessageProvider(ABC):

    @abstractmethod
    def send(self, recipient, message):
        pass