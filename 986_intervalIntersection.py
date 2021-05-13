"""
986. Interval List Intersections
https://leetcode.com/problems/interval-list-intersections/
"""

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # [1] Create a function to compute the intersection of 2 given intervals
        # [2] Iterate through firstList and secondList to compute intersections of the interval
        # [3] Pop the next interval from the list whose right side is farther left.
        # [4] If no other interval is in the lists then assign the next interval to None and break
        # O(min(n,m)) time and space.

        if len(firstList) == 0 or len(secondList) == 0: return []

        ans = []
        l1, l2 = firstList.pop(0), secondList.pop(0)
        while l1 and l2:

            # Get the intersction
            left, right = max(l1[0], l2[0]), min(l1[1], l2[1])
            if left <= right:
                ans.append([left, right])

            # Get the next interval of the list whose right side is farther left
            if l1[1] <= l2[1] and firstList:
                l1 = firstList.pop(0)
            elif l2[1] <= l1[1] and secondList:
                l2 = secondList.pop(0)
            elif l1[1] <= l2[1] and not firstList:
                l1 = None
            elif l2[1] <= l1[1] and not secondList:
                l2 = None

        return ans
