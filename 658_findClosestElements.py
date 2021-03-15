"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements/
"""

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) <= k: return arr

        l, r = 0, len(arr) - k
        while l < r:
            m = l + (r - l) // 2
            r_gap = arr[m + k] - x
            l_gap = x - arr[m]

            if r_gap >= l_gap:
                r = m
            else:
                l = m + 1

        return arr[l:l+k]