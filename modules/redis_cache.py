import redis


class Redis:
    """
        Redis Utility Class
    """

    def __init__(self):
        self.r = redis.Redis('localhost', port=6379, db=0, decode_responses=True)

    def append_google_search_history(self, search_val):
        """
            Add search command at head of list
        """
        self.r.lpush('google_search', search_val)

    def get_latest_searches(self):
        """
            Return recent 5 searched commands
        """
        return self.r.lrange('google_search', 0, 4)
