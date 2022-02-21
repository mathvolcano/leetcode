"""
374. Guess Number Higher or Lower
https://leetcode.com/problems/guess-number-higher-or-lower/
"""

class Solution(object):
    def guessNumber(self, n):
        # Perform a binary search
        l, r = 1, n
        while l <= r:
            m = (l+r) // 2
            high_or_low_or_right = guess(m)
            if high_or_low_or_right == 1:
                l = m + 1
            elif high_or_low_or_right == -1:
                r = m - 1
            else:
                return m
        return l
