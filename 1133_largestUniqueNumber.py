"""
1133. Largest Unique Number
https://leetcode.com/problems/largest-unique-number/
"""

class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        # O(n) because we have to count every element
        from collections import Counter
        counts = Counter(A)
        keys = [x for x in counts if counts[x] == 1]
        return -1 if len(keys) == 0 else max(keys)