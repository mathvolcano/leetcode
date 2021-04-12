"""
1394. Find Lucky Integer in an Array
https://leetcode.com/problems/find-lucky-integer-in-an-array/
"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        counts = Counter(arr)
        luckies = [c for c in counts if counts[c] == c]
        return -1 if not luckies else max(luckies)
