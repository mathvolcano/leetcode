"""
1200. Minimum Absolute Difference
https://leetcode.com/problems/minimum-absolute-difference/
"""

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # O(n log n) because we need to sort
        arr.sort()
        min_abs_diff = min([arr[i] - arr[i-1] for i in range(1, len(arr))])

        pairs = []
        for i, a in enumerate(arr[1:], start=1):
            if (a - arr[i-1]) == min_abs_diff:
                pairs.append([arr[i-1], a])
        return pairs
