import redis


class Redis:

    def __init__(self):
        self.r = redis.Redis('localhost', port=6379, db=0, decode_responses=True)

    def append_google_search_history(self, search_val):
        self.r.lpush('google_search', search_val)

    def get_latest_searches(self):
        return self.r.lrange('google_search', 0, 4)
