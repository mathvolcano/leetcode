"""
633. Sum of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers/
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # O(n) solution – iterate through all squares and check if c - square is a perfect square.
        # squares = [n*n for n in range(c+1)]
        # for s in squares:
        #     if c-s in squares:
        #         return True
        # return False

        # O(log(n)) using binary search
        if c in (0,1,2): return True

        l, r = 0, int(c**0.5)
        while l <= r:
            cur = l**2 + r**2
            if cur < c:
                l += 1
            elif cur > c:
                r -= 1
            else:
                return True
        return False
