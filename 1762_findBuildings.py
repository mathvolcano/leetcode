"""
1762. Buildings With an Ocean View
https://leetcode.com/problems/buildings-with-an-ocean-view/
"""
class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:

        # Monotone stack
        # [0] initialize stack, s = []
        # [1] Iterate from right to left
        #  a. if stack empty or element is smaller than s[-1][1] then continue
        #  b. else append index & height to stack
        # [2] return list of indices reversed from stack
        # O(n) time (best, worst, average) and O(n) space (worst case, need to store all indices)
        s = []
        for i in range(len(heights)-1, -1, -1):
            if not s or heights[i] > s[-1][1]:
                s.append((i, heights[i]))
        return [x[0] for x in s[::-1]]
