"""
1306. Jump Game III
https://leetcode.com/problems/jump-game-iii/
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0: return True

        q = [start]
        visited = [0] * len(arr)
        while q:
            cur = q.pop(0)
            if arr[cur] == 0:
                return True
            else:
                visited[cur] = 1
                next_levels = [cur - arr[cur], cur + arr[cur]]
                for v in next_levels:
                    if (0 <= v < len(arr)) and visited[v] == 0:
                        q.append(v)
        return False
