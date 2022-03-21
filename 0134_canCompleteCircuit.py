"""
134. Gas Station
https://leetcode.com/problems/gas-station/
"""

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # Greedy Algorithm
        # [1] Initiate total_tank and curr_tank as zero, and choose station 0 as a starting station.
        # [2] Iterate over all stations
        #     a) Update total_tank and curr_tank at each step, by adding gas[i] and subtracting cost[i].
        #     b) If curr_tank < 0 at i + 1 station, make i + 1 station a new starting point and reset curr_tank = 0 to start with an empty tank.
        # O(n) time complexity and O(1) space


        n = len(gas)
        tot_tank, cur_tank, station = 0, 0, 0
        for i in range(n):
            tot_tank += gas[i] - cost[i]
            cur_tank += gas[i] - cost[i]
            if cur_tank < 0:
                station = i + 1
                cur_tank = 0
        return station if tot_tank >= 0 else -1
