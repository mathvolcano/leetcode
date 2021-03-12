"""
704. Binary Search
https://leetcode.com/problems/binary-search/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """O(log(n))"""
        if target < nums[0] or target > nums[-1]: return -1
        if target == nums[0]: return 0
        if target == nums[-1]: return len(nums) - 1

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:  # target < mid
                r = m - 1
        return -1

        # try:
        #     return nums.index(target)
        # except ValueError:
        #     return -1
