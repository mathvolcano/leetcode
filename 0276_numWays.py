"""
276. Paint Fence
https://leetcode.com/problems/paint-fence/
"""

class Solution:
    def numWays(self, n: int, k: int) -> int:

        # DP
        # numWays(1, k) = k
        # numWays(2, k) = k * (k-1)
        # Note that the number of ways of making the next post the same color
        # as the previous post is same = diff because the next post's color is determined
        # Similarly, the number of ways to make the next post is different is equal to
        # diff = (same + diff) * (k-1)
        # Time complexity: O(n), space complexity O(1)

        if n == 1: return k
        if n == 2: return int(k**2) #
        same, diff = k, k * (k-1)
        for i in range(3, n+1):
            same, diff = diff, (same + diff) * (k-1)
        return int(same + diff)