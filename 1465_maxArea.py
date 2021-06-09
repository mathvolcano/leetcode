"""
1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
"""

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        # [1] Sort the cut arrays
        # [2] Add the endpoints of the area 0 and h or 0 and w to the cut arrays
        # [3] Find the max difference between consecutive elements cuts in the array.

        # Example: h = 5, w = 4, horizontalCuts = [1,4,2], verticalCuts = [1,3]
        # After sort: horizontalCuts = [1,2,4], verticalCuts = [1,3]
        # After adding endpoints horizontalCuts = [0,1,2,4,5], verticalCuts = [0,1,3, 4]
        # max_h_diff = 2 (4-2)
        # max_v_diff = 2 (3-1)
        # return 4 % (10**9 + 7)
        # O(h log h + v log v + h*v) time complexity where h = len(horizontalCuts) and v = len(verticalCuts) with O(1) additional space

        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        max_h_diff, max_v_diff = 0, 0
        for i in range(1, len(horizontalCuts)):
            max_h_diff = max(max_h_diff, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            max_v_diff = max(max_v_diff, verticalCuts[i] - verticalCuts[i-1])
        return (max_h_diff * max_v_diff) % 1000000007
