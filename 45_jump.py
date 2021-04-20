"""
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        # "BFS" – O(n) time complexity, O(1) space.
        steps, near, far = 0, 0, 0
        for i in range(len(nums)):
            if i > near:
                steps += 1
                near = far
            far = max(far, i + nums[i])
        return steps


        # BFS Long – O(n) time and space complexity
        # n, jumps = len(nums), 0
        # if n == 1: return jumps
        #
        # # DP / BFS
        # level = set()
        # level.add((0, nums[0]))
        # visited = [0] * n
        # while level:
        #     nxt_level = set()
        #     jumps += 1
        #     for i, v in level:
        #         if i + v >= n - 1:
        #             return jumps
        #         elif v == 0:
        #             pass
        #         else:  # i + v < n
        #             reachable = [(j, k) for j, k in enumerate(nums[i: i+1+v], start=i) if visited[j] != 1]
        #             for r in reachable:
        #                 nxt_level.add(r)
        #         visited[i] = 1
        #     level = nxt_level
        # return
