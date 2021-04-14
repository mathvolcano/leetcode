"""
1064. Fixed Point
https://leetcode.com/problems/fixed-point/
"""

class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        # Binary Search O(log n) time
        n = len(arr)
        if n == 1: return arr[0] if arr[0] == 0 else -1
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] - m < 0:
                l = m + 1
            else:  # arr[m] > m
                r = m
        return l if arr[l] == l else -1


        # O(n) time and space
        # Pythonic
        # for i,n in enumerate(arr):
        #     if i == n:
        #         return i
        # return -1
