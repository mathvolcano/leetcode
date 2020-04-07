"""
Counting Elements
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/
"""


class Solution:
    def countElements(self, arr: List[int]) -> int:
        from collections import Counter
        if len(arr) <= 1: return 0

        counts = Counter(arr)

        total_count = 0
        for x in counts:
            if x + 1 in counts:
                occ = counts[x]
                total_count += occ
        return total_count
