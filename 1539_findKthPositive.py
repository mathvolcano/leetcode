"""
1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/
"""

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        # Have to check each entry of arr up to k:
        # O(n) time complexity
        # But only need to track the missing element up to k
        # O(1) space complexity

        n_missing = 0
        a, p = 0, 1
        while p < arr[-1]:
            if arr[a] == p:
                a += 1
            else:
                n_missing += 1
                if n_missing == k:
                    return p
            p += 1

        return p + (k - n_missing)
