"""
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/
"""

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # Heap solution O(n log n)
        from heapq import heappushpop, heappush
        if len(intervals) == 1: return 1

        size = len(intervals)
        if size <= 1: return size
        heap = []
        for i in sorted(intervals):
            if heap and i[0] >= heap[0]:
                heappushpop(heap,i[1])
            else:
                heappush(heap,i[1])
        return len(heap)

        # # 1. Sort intervals by start time
        # # 2. Have a hall of rooms, exit hall after time has elapsed
        # # 3. Return the length of the hall
        # # O(n log n) time needed for sort. O(n) space needed
        #
        if len(intervals) == 1: return 1
        # intervals.sort(key=lambda x: x[0])
        # hall = [[]]
        # for j, span in enumerate(intervals):
        #     found = 0
        #     for i, room in enumerate(hall):
        #         if (len(room) == 0) or (span[0] >= room[1]):
        #             hall[i] = span
        #             found = 1
        #             break
        #     if found == 0:
        #         hall = hall + [span]
        # return len(hall)


