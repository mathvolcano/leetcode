"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    n = len(intervals)
    if n == 1: return intervals

    intervals.sort(key=lambda x: x[0])
    l_idx, r_idx = 0, 1
    while r_idx < n:
        l, r = intervals[l_idx], intervals[r_idx]
        if r[0] <= l[1]:
            new_int = [l[0], max(l[1], r[1])]
            intervals[l_idx] = new_int
            intervals.pop(r_idx)
            n -= 1
        else:
            l_idx += 1
            r_idx += 1
    return intervals