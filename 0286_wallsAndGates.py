"""
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/
"""

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # Perform a BFS

        # macros
        empty = 2147483647
        wall = -1
        gate = 0
        n_rows, n_cols = len(rooms), len(rooms[0])


        def valid_directions(i,j):
            nsew = [(i,j+1), (i,j-1), (i+1,j), (i-1,j)]
            return [x for x in nsew if (0 <= x[0] <= n_rows-1) and (0 <= x[1] <= n_cols-1)]

        # store all nodes which are waiting to be processed
        q = []  # queue
        for i in range(n_rows):
            for j in range(n_cols):
                if rooms[i][j] == gate:
                    q.append([i,j])

        while q:
            new_q = []
            for i,j in q:
                cur_dist = rooms[i][j]

                # Add neighbors to queue
                neighbors = valid_directions(i, j)
                for ne in neighbors:
                    if rooms[ne[0]][ne[1]] == empty:
                        rooms[ne[0]][ne[1]] = cur_dist + 1
                        new_q.append(ne)

            # Add unique unexplored neighbors to queue
            new_unique_rooms = list(set(new_q))
            q = new_unique_rooms  # Unique rooms

        # Any remaining empty rooms cannot reach gate
        rooms = [[v if v <= empty else -1 for v in r] for r in rooms]