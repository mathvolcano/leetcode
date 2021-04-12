"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""

class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        if n in cache: return self.fib(cache)

        if n < 2:
            res = n
        else:
            res = self.fib(n-1) + self.fib(n-2)
        cache[n] = res
        return res
