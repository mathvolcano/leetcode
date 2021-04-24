"""
252. Meeting Rooms
https://leetcode.com/problems/meeting-rooms/
"""
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # O(n log n) time for sort.
        if len(intervals) == 1: return True
        intervals.sort(key=lambda x: x[0])

        for j, i in enumerate(intervals[1:], start=1):
            p = intervals[j-1]  # previous
            if p[1] > i[0]:
                return False
        return True
