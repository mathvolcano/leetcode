class LRUCache:

    def __init__(self, capacity: int):
        from collections import OrderedDict
        self.cache = []  # least used at front of queue
        self.capacity = capacity
        self.n_cached = 0

    def get(self, key: int) -> int:
        for x in range(self.n_cached):
            if key == self.cache[x][0]:
                kv = self.cache.pop(x)
                self.cache.append(kv)
                return kv[1]
        return -1

    def put(self, key: int, value: int) -> None:

        # set value if key already present
        for x in range(self.n_cached):
            if key == self.cache[x][0]:
                self.cache[x] = (key, value)

                kv = self.cache.pop(x)
                self.cache.append(kv)
                return

        # Add kv if not present
        if self.n_cached < self.capacity:
            self.cache.append((key, value))
            self.n_cached += 1
        # Remove least used
        else:
            removed = self.cache.pop(0)
            self.cache.append((key, value))
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)