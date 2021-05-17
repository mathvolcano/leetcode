"""
1197. Minimum Knight Moves
https://leetcode.com/problems/minimum-knight-moves/
"""

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        # BFS
        # [1] Create a queue with initial location in it.
        # [2] Add conditions to deal with symmetry and only work in quadrant 1
        # [3] Track whether a position was reached in a hash_set
        # [4] Iterate through the queue and check if they are the target
        # if so end else compute neighbors
        # [5] Check if neighbors are in visited, if not add to queue.
        # O(nm) time and space complexity worst case (storing hash_set and searching the full grid).

        directions = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]

        import collections
        q = collections.deque()
        q.append((0, 0, 0))

        x, y = abs(x), abs(y)  # By symmetry
        # Add condition to deal with symmetry
        if x == 1 and y == 1: return 2
        steps = 0
        visited = set((0,0))

        while q:
            px, py, steps = q.popleft()
            if px == x and py == y: return steps
            for dx, dy in directions:
                new_px, new_py = px + dx, py+dy
                if 0 <= new_px<= 300 and 0 <= new_py <= 300 and (new_px, new_py) not in visited:
                    visited.add((new_px, new_py))
                    q.append((new_px, new_py, steps+1))
        return steps
