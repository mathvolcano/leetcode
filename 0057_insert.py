"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0: return [newInterval]

        result = []

        # Get the first interval where left newInterval is bigger than right
        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Get the maximum overlap of newInterval with intervals
        l, r = newInterval
        while i < n and intervals[i][0] <= newInterval[1]:
            l = min(l, intervals[i][0])
            r = max(r, intervals[i][1])
            i += 1

        # Add the overlapping new Interval and then the rest of the non-overlapping intervals bigger than it
        result.append([l, r])
        result.extend(intervals[i:])
        return result



