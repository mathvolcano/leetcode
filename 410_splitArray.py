"""
410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        # Binary Search & DP
        # [1] Note that the valid answers vary in the range [max(nums), sum(nums)]
        # because every subarray must at least include max(nums) and no single subarray
        # can exceed sum(nums). So we binary search this range
        # [1a] if we find that the searched val is valid, set to ans and increase values of search.
        # [1b] else, decrease range
        # [2] To check if a number, mid, is valid, count the number of continuous subarrays that do not exceed mid in sum. If this number exceeds m then return false. Else return true
        # sum does not exceed mid
        # O(log(sum(nums) - max(nums)) * len(nums)) time complexity, O(1) space

        def is_valid(nums, m, mid):
            subarrs, cur = 1, 0
            for n in nums:
                cur += n
                if cur > mid:
                    subarrs, cur = subarrs + 1, n
            return (subarrs <= m)

        l, r = max(nums), sum(nums)
        while l <= r:
            mid = (l + r) // 2
            if is_valid(nums, m, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l
