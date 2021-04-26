"""
1642. Furthest Building You Can Reach
https://leetcode.com/problems/furthest-building-you-can-reach/
"""

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        from heapq import heappush, heappop
        # Iterate over next buildings and keep track of min height difference
        # using a heap.
        # Use ladders only on the largest heights. Use a min heap
        # of length the ladders and apply bricks on the min heights
        # The max height diff will be used for a ladder.
        h = []  # Python uses a min heap by default
        # O(n lg n) for time and O(n) space
        n = len(heights)
        if n == 1: return 1
        for i in range(n - 1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                if ladders > 0:
                    heappush(h, diff)
                    ladders -= 1
                elif h and diff > h[0]:
                    heappush(h, diff)
                    bricks -= heappop(h)
                else:
                    bricks -= diff
                if bricks < 0: return i
        return n - 1
