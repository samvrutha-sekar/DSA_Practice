class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

    def get(self, key_):
        if key_ not in self.cache:
            return -1

        value = self.cache.pop(key_)
        self.cache[key_] = value
        return value

    def put(self, key_, value):
        if key_ in self.cache:
            self.cache.pop(key_)
        elif len(self.cache) >= self.capacity:
            oldest = next(iter(self.cache))
            self.cache.pop(oldest)

        self.cache[key_] = value