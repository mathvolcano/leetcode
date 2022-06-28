"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # [1] Sort meetings
        # [2] Initialize a result variable res = 1 and a min heap, h = []
        # [3] Iterate m through intervals
        # [4] while h and m starts after the first element of h ends, heappop(h)
        # [5] else, heappush(h, m.end)
        # [3] Update result object as length of heap
        # [4] return res
        # Complexity:
        # Time: O(n log n) time complexity for sort, iterations & heaps are at worst O( n * log n) => Final O( n lg n)
        # Space: O(n) worst case when all meetings have conflicts to store in heap h, but can make additional space O(1) by popping meetings
        # but would still need O(n) space for the sorting operation.
        from heapq import heappop, heappush
        n = len(intervals)
        if n <= 1: return n
        res, h = 0, []
        for m in sorted(intervals):  # meeting
            while h and m[0] >= h[0]:
                heappop(h)
            heappush(h, m[1])
            res = max(res, len(h))
        return res


