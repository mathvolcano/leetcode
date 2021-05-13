"""
1354. Construct Target Array With Multiple Sums
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
"""

class Solution:
    def isPossible(self, target: List[int]) -> bool:

        # [1] Use a max heap (priority queue)
        # [2] Remove the max value
        # [3] compute the max val's replacement's value
        # [4]  reinsert smaller max back into pq.
        # [5a] If we see that the max value in pq is a 1, then that means that all values in pq are 1s, and we should return true.
        # [5b] else return False
        # O(n log n) time for heapsort, O(log n) space on average (for stored max values)

        # [1]
        from heapq import heapify, heappush, heappop
        h = [-t for t in target]  # heap
        total = sum(target)
        heapify(h)

        # [2]-[5]
        while h[0] != -1:
            v = -heappop(h)
            total -= v
            if v <= total or total < 1: return False
            v %= total
            total += v
            heappush(h, -v or -total)
        return True
