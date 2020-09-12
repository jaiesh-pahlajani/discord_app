from modules.message_handling.base_message import Message
from modules.redis_cache import Redis
from discord_bot.enums import (
    DoloresReceives,
    DoloresReplies
)


class Recent(Message):
    """
        Handles message starting with google
    """

    def __init__(self, message):
        super(Recent, self).__init__(message)
        self.redis = Redis()

    def handle(self):
        prefix = 'Top 5 recent search keywords are: \n-'
        if self.message == DoloresReceives.RECENT.value:
            search_list = self.redis.get_latest_searches()
            search_history = '\n- '.join(search_list)
        else:
            return DoloresReplies.RECENT_HANDLING.value
        return prefix + search_history
