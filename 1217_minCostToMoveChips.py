"""
1217. Minimum Cost to Move Chips to The Same Position
https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/
"""
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        # [0] Initialize a dic of parities {}
        # [1] For each parity, 0 or 1, count the number of chips that have the parity.
        # [2] Return the min of the counts

        # Example 1:
        # [0] parities = {0: 0, 1:0}
        # parities = {0: 1, 1: 2}
        # return min(1,2) = 1

        from collections import defaultdict
        parities = defaultdict(int)
        for p in position:
            parities[p % 2] += 1
        return min(parities[0], parities[1])
