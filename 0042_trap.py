"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        # 2 pointer
        # For a given point in the array its area is found by taking
        # the smaller of the highest wall
        # to the left or right of it and subtracting the height.
        # height = [0,1,0,2,1,0,1,3,2,1,2,1]
        # l_max  = [0,1,1,2,2,2,2,3,3,3,3,3]
        # r_max  = [3,3,3,3,3,3,3,3,2,2,2,1]
        # area   = [0,0,1,0,1,2,1,0,0,1,0,0]
        # Time complexity: O(n)
        # Space complexity: O(n)

        n = len(height)
        if n <= 1: return 0

        l_max = [0] * n
        l_max[0] = height[0]
        for l in range(1, n):
            l_max[l] = max(l_max[l-1], height[l])

        r_max = [0] * n
        r_max[-1] = height[-1]
        for r in range(n-2, -1, -1):
            r_max[r] = max(r_max[r+1], height[r])

        area = 0
        for i in range(n):
            area += min(l_max[i], r_max[i]) - height[i]
        return area
