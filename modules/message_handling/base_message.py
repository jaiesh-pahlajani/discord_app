from abc import ABC, abstractmethod


class Message(ABC):
    """
        Base Message Class
    """
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def handle(self):
        pass
