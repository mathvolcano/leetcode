"""
77. Combinations
https://leetcode.com/problems/combinations/
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(arr, k, res, path):
            if k > len(arr):
                return
            if k == 0:
                res.append(path)
            else:
                helper(arr[1:], k - 1, res, path + [arr[0]])
                helper(arr[1:], k, res, path)

        res = []
        helper(range(1, n + 1), k, res, [])
        return res
