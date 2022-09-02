"""
241. Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/
"""
class Solution:
    def diffWaysToCompute(self, s, memo={}) -> List[int]:
        # DFS Backtrack
        # [0] Initialize a helper to calculate operation between 2 arguments
        # [1] if s is digit return [int(s)]
        # [2] if s is in a memoization (cache) then return cache
        # [3] for i in range(len(s)) if s[i] is an operation then split string s at i and run self.diffWaysToCompute on s[:i] and s[i+1:] and store as res1, res2 resp
        # [4] for j,k in res1, res2 append to result helper(j,k, s[i]).
        # Complexity n = len(s)
        # Bijection with balanced parentheses
        # Time: O(n*2^n) (or Catalan numbers) because at each number can open/close a parentheses
        # and splitting the string takes n time.
        # Space: O(2^n) worst to store results (catalan numbers)
        if s.isdigit():
            return [int(s)]
        if s in memo:
            return memo[s]
        res = []
        for i in range(len(s)):
            if s[i] in "-+*":
                res1 = self.diffWaysToCompute(s[:i])
                res2 = self.diffWaysToCompute(s[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, s[i]))
        memo[s] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
