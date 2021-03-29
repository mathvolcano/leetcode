"""
81. Search in Rotated Sorted Array II
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        # print(n, nums[0], target)
        if n == 1: return nums[0] == target

        # 1. Binary Search O(log(n)) to find pivot
        l, r = 0, n-1
        while l <= r:
            # Get the highest l for which we have a different l & r value to remove indices with the same values.
            while (l < r) and (nums[l] == nums[r]):
                l += 1

            m = (l + r) // 2
            # Check if accessed values are target
            if target == nums[m]:
                return True

            if (nums[m] >= nums[l]):  # Left maybe sorted
                if nums[l] <= target < nums[m]:  # Target is left of mid
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] <= nums[r]:  # Right maybe sorted
                if nums[m] < target <= nums[r]:  # Sorted & search right:
                    l = m + 1
                else:  # Search right for target
                    r = m - 1

        return False