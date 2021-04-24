"""
1094. Car Pooling
https://leetcode.com/problems/car-pooling/
"""
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Heap solution O(n log n)
        from heapq import heappush, heappop
        if len(trips) == 1: return True
        trips.sort(key=lambda x: x[1])

        h = []  # Use a min heap with [end_location, num_passengers]
        for t in trips:

            # Dropoff Passengers
            while h and h[0][0] <= t[1]:
                capacity += h[0][1]
                heappop(h)

            # Check capacity
            if (capacity - t[0] >= 0):
                heappush(h, [t[2], t[0]])
                capacity -= t[0]
            else:
                return False
        return True
