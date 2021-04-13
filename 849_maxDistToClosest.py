"""
849. Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        # O(n) time and space
        n = len(seats)

        l_dist = [0] * n
        last_l_seat = float('inf')
        for l, s in enumerate(seats):
            if seats[l] == 0:
                last_l_seat += 1
            else:
                last_l_seat = 0
            l_dist[l] = last_l_seat

        r_dist = [0] * n
        last_r_seat = float('inf')
        for r, s in enumerate(reversed(seats), start=1):
            if seats[n-r] == 0:
                last_r_seat += 1
            else:
                last_r_seat = 0
            r_dist[n-r] = last_r_seat

        dist = [min(l_dist[i], r_dist[i]) for i in range(n)]
        return max(dist)
