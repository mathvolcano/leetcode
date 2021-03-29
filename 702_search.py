"""
702. Search in a Sorted Array of Unknown Size
https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/
"""

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        # Perform a binary search where we set l & r to the smallest dyadic range containing target.
        r = 1
        while reader.get(r) < target:
            r *= 2
        l = r // 2

        while l <= r:
            m = l + (r - l) // 2
            val = reader.get(m)
            if val == target:
                return m
            elif val > target:
                r = m - 1
            else:  # val < target
                l = m + 1
        return -1
