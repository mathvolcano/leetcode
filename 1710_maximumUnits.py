"""
1710. Maximum Units on a Truck
https://leetcode.com/problems/maximum-units-on-a-truck/
"""

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        # Greedy algorithm
        # [1] Sort boxes by the number of units
        # [2] Add the number of units in the next largest box to a result counter
        # decrement trucksize until either the number of boxTypes is empty or the
        # truckSize is empty.

        boxTypes.sort(key=lambda x: -x[1])

        res = 0
        for t, u in boxTypes:
            if truckSize > t:
                truckSize -= t
                res += t * u
            else:
                res += truckSize * u
                return res
        return res
