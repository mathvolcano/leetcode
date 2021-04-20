"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/
"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(cur, path):
            if cur == 0:
                res.append(path)
            for n in candidates:
                if n > cur:
                    break
                if path and n < path[-1]:
                    continue
                dfs(cur - n, path + [n])

        res = []
        candidates.sort()
        dfs(target, [])
        return res

        # BFS
        # res = [(c) for c in candidates if c == target]
        # level = [[c] for c in candidates if c != target]
        # while level:
        #     l = level.pop(0)
        #     tot = sum(l)
        #     for c in candidates:
        #         concat = l + [c]
        #         s = tot + c
        #         if s == target:
        #             concat.sort()
        #             res.append(tuple(concat))
        #         elif s < target:
        #             level.append(concat)
        # return [[r] if type(r) is int else list(r) for r in set(res)]
