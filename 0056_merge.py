"""
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # [1] Sort intervals by start_i
        # [2] Initialize left & right indices, l_idx, r_idx = 0, 1 to track intervals
        # [3] loop through intervals
        #  a. compare the 1st index of r_idx interval against the 2nd index of intervals[l_idx]
        #  b. Case 1 <=: then get new interval [l[0], max(l[1], r[1])
        #. c. update intervals[l_idx] to be the new intervals
        #. d. pop intervals[r_idx]
        #  e. Case 2 > : increment l_idx and r_idx because intervals do not intersect.
        # [4] return intervals

        # Time complexity: O(n log n)
        # Space complexity: O(1)
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
