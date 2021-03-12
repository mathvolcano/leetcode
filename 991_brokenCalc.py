"""
991. Broken Calculator
https://leetcode.com/problems/broken-calculator/
"""

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y

        n_ops = 0
        while X < Y:
            if Y % 2 == 1:
                Y += 1
                n_ops += 1
            Y //= 2
            n_ops += 1

        return n_ops + X - Y
