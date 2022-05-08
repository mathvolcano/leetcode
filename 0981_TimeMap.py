"""
981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/
"""
class TimeMap:

    def __init__(self):
        from collections import defaultdict
        # Hashmap
        # Store as {key: [timestamp, value]}
        self.h = defaultdict(list)


    def set(self, k: str, v: str, ts: int) -> None:
        # Append to end because all timestamps of set are strictly increasing
        # O(1) time, O(n) space where n is the number of set operations
        self.h[k].append([ts,v])


    def get(self, key: str, timestamp: int) -> str:
        # Perform binary search O(log n) worst case
        # where n is the number of set operations of the answer
        if key not in self.h: return ''
        a = self.h[key]  # arr
        l, r = 0, len(a)
        while l < r:
            m = (l + r) // 2
            tsm = a[m][0]
            if tsm > timestamp:
                r = m
            else:
                l = m + 1
        return '' if r == 0 else a[m][1]



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)