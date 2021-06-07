"""
815. Bus Routes
https://leetcode.com/problems/bus-routes/
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        # BFS
        # [0] Create a lookup of destination to route index
        # [1] initialize a result integer that counts the min number of hops needed
        # [2] initialize a queue with source
        # [3] for each stop in queue get the route indices it connects with
        # [4] get all stops on these connecting route indices
        # [5] For each route index check if route index is visited
        # and if so skip it, else add all stops on the route to the next level of queue
        # as long as the stop is not the current one.
        # [6] increment result

        # Ex [[1,2,7],[3,6,7]], source=1, target=6
        # place_to_route = {1:0, 2:0, 3:1, 6:1, 7:[0,1]}
        # q = [1], visited = set()
        # After 1st search: visited=set(0,1), new_q = [2,7], res =1

        # Time complexity: O(r * max(stops on routes)) because we visited all nodes in worst case
        # Space complexity: same because worst case we store all stops

        from collections import defaultdict
        stop_to_route = defaultdict(set)
        for i, r in enumerate(routes):
            for stop in r:
                stop_to_route[stop].add(i)

        res = 0          # result
        visited = set()  # stops visited
        q = [source]     # queue
        while q:
            new_q = []
            for stop in q:
                if stop == target:
                    return res
                for r in stop_to_route[stop]:
                    if r not in visited:
                        visited.add(r)
                        for new_stop in routes[r]:
                            if new_stop != stop:
                                new_q.append(new_stop)
            q = new_q
            res += 1
        return -1
