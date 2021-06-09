"""
490. The Maze
https://leetcode.com/problems/the-maze/
"""

class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # BFS
        # [1] Create a helper that gets next positions of the ball
        # [1a] create a results list of tuples and a set of used places
        # [1b] For each NSEW direction continue to add a single direction step to the start position until a wall is reached
        # [1c] check if the resulting position is already in the result. If not add it (e.g., corner).
        # [2] Perform a BFS search to track if we've landed on destination
        # [2a] Create a visited hash set of positions (tuples) to track that the ball has been
        # [2b] create a queue to track the number of spaces moved and the position
        # Iteration
        # [2c] popleft next step count & position.
        # [2d] check if position is in visited. if so skip
        # [2e] check position is the destination if so then return True
        # [2f] else, get neighbors and neighbor distance and enque them.

        # Time complexity: O(m*n) time and space because we may have to search
        # up to all squares.


        start, destination = tuple(start), tuple(destination)
        self.m, self.n = len(maze), len(maze[0])

        def neighbors(maze, pos):
            res, used = [], set()
            used.add(pos)
            for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                x,y = pos
                while 0 <= x+dx < self.m and 0 <= y+dy < self.n and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                if (x,y) not in used:
                    res.append((x,y))
            return res

        visited = set()
        from collections import deque
        q = deque([start])
        while q:
            print('q', q)
            pos = q.popleft()
            if pos in visited: continue
            if pos == destination: return True
            visited.add(pos)
            for n in neighbors(maze, pos):
                q.append(n)
        return False
