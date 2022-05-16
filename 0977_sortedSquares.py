"""
977. Squares of a Sorted Array
https://leetcode.com/problems/squares-of-a-sorted-array/
"""

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Use 2 points at beginning and end. Compare which is larger and append to result
        # O(n)
        res = []
        l, r = 0, len(nums) - 1
        while l <= r:
            nl2, nr2 = nums[l]**2, nums[r]**2
            if nl2 <= nr2:
                res.insert(0, nr2)
                r -= 1
            elif nl2 > nr2:
                res.insert(0, nl2)
                l += 1
        return res

        # Pythonic O(n log n) because it performs a sort
        # return sorted(x*x for x in nums)
