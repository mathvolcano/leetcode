"""
505. The Maze II
https://leetcode.com/problems/the-maze-ii/
"""

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:

        # BFS
        # [1] Create a helper that gets next positions of the ball
        # [1a] create a results list of tuples and a set of used places
        # [1b] For each NSEW direction continue to add a single direction step to the start position until a wall is reached
        # [1c] Count the distance between start and wall
        # [1d] check if the resulting position is already in the result. If not add it.
        # [2] Perform a BFS search to track how many squares the ball moves to
        # get to the goal
        # [2a] Create a visited set of positions to track that the ball has been
        # to after so many moves
        # [2b] create a heap to track the number of spaces moved and the position
        # Iteration
        # [2c] heappop next step count & position.
        # [2d] check if position is in visited. if so skip
        # [2e] check position is the destination if so then return steps
        # [2f] else, get neighbors and neighbor distance and heappush to heap.

        # Time complexity: O(m*n) time and space because we may have to search
        # up to all squares.


        start, destination = tuple(start), tuple(destination)
        self.m, self.n = len(maze), len(maze[0])

        def neighbors(maze, pos):
            res, used = [], set()
            used.add(pos)
            for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                (x,y), dist = pos, 0
                while 0 <= x+dx < self.m and 0 <= y+dy < self.n and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    dist += 1
                if (x,y) not in used:
                    res.append((dist, (x,y)))
            return res

        visited = set()
        from heapq import heappop, heappush
        h = [(0, start)]  # (steps, pos)
        while h:
            steps, pos = heappop(h)

            if pos in visited: continue
            if pos == destination: return steps
            visited.add(pos)

            for s, n in neighbors(maze, pos):
                heappush(h, (steps+s, n))
        return -1
