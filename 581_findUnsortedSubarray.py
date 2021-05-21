"""
581. Shortest Unsorted Continuous Subarray
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
"""

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:


        # [1] set l to be the last index from the right with value bigger than the min from the right
        # [2] set r to be the last index from the  left with value bigger than the max from the  left
        # Ex, [2,6,4,8,10,9,15]
        # max from left  [2, 6, 6, 8, 10, 10, 15]
        # min from right [2, 4, 4, 8,  9,  9, 15]
        # Here l = 1 and r = 5, and we return r - l + 1
        # O(n) time and O(1) space

        n = len(nums)
        if n == 1: return 0

        r, l = -1, -1
        lmax, rmin = nums[0], nums[-1]
        for i in range(1, n):
            lval, rval = nums[i], nums[n-i-1]
            if lval < lmax:
                r = i
            else:
                lmax = max(lval, lmax)
            if rval > rmin:
                l = n-i-1
            else:
                rmin = min(rval, rmin)
        return 0 if r == l else r - l + 1

        # Sort
        # [1] Create a copy of nums & sort -> nums2
        # [2] Get the first and last indices where nums and nums2 differ
        # O(n log n) time complexity for sort and O(n) space

#         nums2 = nums.copy()
#         nums2.sort()

#         n = len(nums)
#         diff_indices = [i for i in range(n) if nums[i] != nums2[i]]
#         if not diff_indices:
#             return 0
#         l = min(diff_indices)
#         r = max(diff_indices)
#         return r - l + 1
