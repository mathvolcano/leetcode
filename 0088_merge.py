"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 2 pointers

        # 1 Set a pointer, last, to the last position of nums (m+n-1)
        # 2 While m >= 0 and n >= 0, set nums1[last] to max(nums1[m], nums2[n])
        # 3 Decrement n if nums2[n] >= nums1[m]
        # 4 Decrement last
        # 5 If any elements in nums2 are remaining (n >= 0), fill nums1[last]
        #   with remaining elements.
        # O(m + n) time complexity and O(1) space

        # 1
        last = m + n -1
        m -= 1
        n -= 1

        # 2
        while m >= 0 and n >= 0:
            # 3
            if nums1[m] > nums2[n]:
                nums1[last] = nums1[m]
                m -= 1
            else:
                nums1[last] = nums2[n]
                n -= 1
            # 4
            last -= 1

        while n >= 0:
            nums1[last] = nums2[n]
            n -= 1
            last -= 1
