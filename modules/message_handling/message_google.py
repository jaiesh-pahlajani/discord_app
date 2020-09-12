from googleapiclient.discovery import build
from modules.message_handling.base_message import Message
from discord_bot.settings import GOOGLE_SEARCH_API_KEY
from modules.redis_cache import Redis


class Google(Message):
    """
        Handles message starting with google
    """

    def __init__(self, message):
        super(Google, self).__init__(message)
        self.resource = build("customsearch", 'v1', developerKey=GOOGLE_SEARCH_API_KEY).cse()
        self.redis = None

    def handle(self):
        query = self.message[8:]
        self.redis = Redis()
        self.redis.append_google_search_history(query)
        results = self.resource.list(q=query, cx='009557628044748784875:5lejfe73wrw').execute()
        c = 0
        reply = ''
        for result in results.get('items'):
            if c < 5:
                reply += "Title: " + result.get('title') + " Link: " + result.get('link') + '\n'
            else:
                break
            c += 1
        return reply
