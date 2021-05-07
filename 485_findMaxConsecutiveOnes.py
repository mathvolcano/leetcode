"""
485. Max Consecutive Ones
https://leetcode.com/problems/max-consecutive-ones/
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # [1] Iterate through array and track the highest consecutive count of ones
        # [2] If we encounter a 1 then add to the current count
        # [3] if we encounter a 0 then set the current count to 0
        # O(n) time complexity and O(1) space
        best, cur = 0, 0
        for n in nums:
            if n == 1:
                cur += 1
            else:
                best = max(best, cur)
                cur = 0
        return max(best, cur)

        # # Brute force - O(n^2) time and space
        # n = len(nums)
        # res = 0
        # pairs = [(i,j) for i in range(n) for j in range(n) if i < j]
        # for i,j in pairs:
        #     subarr = nums[i:j+1]
        #     if sum(subarr) == len(subarr):
        #         res = max(res, len(subarr))
        # return res
