"""
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
"""

class Solution:
    def fib(self, n: int) -> int:
        mem = [0, 1, 1]
        if n < len(mem): return mem[n]
        while len(mem) < n + 1:
            mem += [mem[-1] + mem[-2]]
        return mem[n]
