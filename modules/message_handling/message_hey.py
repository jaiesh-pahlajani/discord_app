from discord_bot.enums import (
    DoloresReceives,
    DoloresReplies
)
from modules.message_handling.base_message import Message


class Hey(Message):
    """
        Handles message starting with Hey
    """

    def __init__(self, message):
        super(Hey, self).__init__(message)

    def handle(self):
        if self.message == DoloresReceives.HEY.value:
            return DoloresReplies.HI.value
        else:
            return DoloresReplies.HI_HANDLING.value
