from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        val = self.cache.get(key) or None
        if val is not None:
            self.cache.move_to_end(key)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
        self.cache.move_to_end(key)

        
