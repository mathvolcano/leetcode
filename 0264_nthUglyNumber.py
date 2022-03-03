"""
264. Ugly Number II
https://leetcode.com/problems/ugly-number-ii/
"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Perform a DP with a list of all ugly numbers known
        # Have 3 pointers to the smallest ugly number s.t.
        # when multiplied is larger than the largest known ugly number
        # Take the min of these numbers multiplied by their coefficients.
        uglies = [1]
        p2 = p3 = p5 = 0
        while len(uglies) < n:
            while uglies[p2]*2 <= uglies[-1]:
                p2 += 1
            while uglies[p3]*3 <= uglies[-1]:
                p3 += 1
            while uglies[p5]*5 <= uglies[-1]:
                p5 += 1
            new_ugly = min(uglies[p2]*2, uglies[p3]*3, uglies[p5]*5)
            uglies.append(new_ugly)
        return uglies[-1]
