"""
528. Random Pick with Weight
https://leetcode.com/problems/random-pick-with-weight/
"""
import random

class Solution:
    # [1] Get the CDF by computing the presums
    # [2] Perform a binary search on the range of integers if we can only select a random int.

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.presum = [w[0]] + ([0] * (self.n-1))
        for i in range(1, self.n):
            self.presum[i] = self.presum[i-1] + w[i]

    def pickIndex(self) -> int:
        total = self.presum[-1]
        rand = random.randint(0, total -1)
        l, r = 0, len(self.presum) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if rand >= self.presum[m]:
                l = m
            else:
                r = m
        if rand < self.presum[l]:
            return l
        return r




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()