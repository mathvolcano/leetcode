"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Use 2 points at beginning and end. Compare which is larger and append to result
        # O(n)
        nums2 = []
        l, r = 0, len(nums) - 1
        while l <= r:
            l_square = nums[l]**2
            r_square = nums[r]**2
            if l_square < r_square:
                nums2.insert(0, r_square)
                r -= 1
            else:
                nums2.insert(0, l_square)
                l += 1
        return nums2

        # Pythonic O(n log n) because it performs a sort
        # return sorted(x*x for x in nums)
