"""
1232. Check If It Is a Straight Line
https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # Check to see if the slopes between each consecutive pair of coordinates
        # has the same slope.

        def slope(c1, c2):
            if c2[0] - c1[0] == 0:
                return float('inf')
            else:
                return (c2[1] - c1[1]) / (c2[0] - c1[0])

        n = len(coordinates)
        if n == 2: return True
        first_slope = slope(coordinates[0], coordinates[1])
        for i in range(2,n):
            if slope(coordinates[i-1], coordinates[i]) != first_slope:
                return False
        return True
