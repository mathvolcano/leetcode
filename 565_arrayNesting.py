"""
565. Array Nesting
https://leetcode.com/problems/array-nesting/
"""

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:

        n = len(nums)
        visited = [False] * n
        res = 0
        for i in range(n):
            cycle = 0
            while not visited[i]:
                cycle += 1
                visited[i] = True
                i = nums[i]
            res = max(res, cycle)
        return res

