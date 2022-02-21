"""
787. Cheapest Flights Within K Stops
https://leetcode.com/problems/cheapest-flights-within-k-stops/
"""

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        # Dijkstra BFS search
        # [1] Create a hash_map graph of the flights
        # [2] Create a distance hash map to lookup if we have visited a stop at smaller cost
        # [3] Create a queue for a BFS search of current stops in the level search
        # [4] Get the first element in the queue by smallest cost using a heappop
        # [5] if the stop is not the best or has too many stops then pass
        # [6] else if the stop is our destination then return cost (the cost is minimal by the sort)
        # [7] else, check all flights in the graph. If the next flight has cost cheaper than the result
        # then add to queue
        # Time complexity O(n^(k+1) log n) where n is the number of flights - because
        # worst case we must search all connecting flights k+1 times with each heappop taking log n time.
        # Space complexity O(n^(k+1)) worst case to store all flights

        from heapq import heappop, heappush
        from collections import defaultdict
        edge = defaultdict(dict)
        for o,d,c in flights:  # origin, destination, cost
            edge[o][d] = c

        dist = {}
        q = [(0, src, 0)]  # cost, cur, k
        while q:
            cost, cur, k = heappop(q)
            if k > K + 1 or cost > dist.get((cur, k), float('inf')):
                continue
            if cur == dst:
                return cost
            for d, c in edge[cur].items():
                tmp = cost + c
                if tmp < dist.get((d, k + 1), float('inf')):
                    heappush(q, (tmp, d, k + 1))
                    dist[(d, k + 1)] = tmp
        return -1
