import hashlib


class QueryCache:

    def __init__(self):
        self.cache = {}

    def _key(self, question: str):
        return hashlib.md5(question.encode()).hexdigest()

    def get(self, question: str):

        key = self._key(question)
        return self.cache.get(key)

    def set(self, question: str, value):

        key = self._key(question)
        self.cache[key] = value