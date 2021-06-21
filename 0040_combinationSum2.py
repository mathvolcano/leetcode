"""
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, start, path):
            if target == 0:
                res.add(path)
            for i, n in enumerate(candidates[start:], start=start):
                if target < n: return
                if i > start and candidates[i] == candidates[i-1]:  # Skip dupes
                    continue
                dfs(candidates, target-n, i+1, path + (n,))

        res = set()
        candidates.sort()
        dfs(candidates, target, 0, tuple())
        return list(res)
