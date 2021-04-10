"""
852. Peak Index in a Mountain Array
https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # Because the arr is guranteed to have a mount, it is combined 2 sorted arrays.
        # So perform a binary search
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) //2
            if (arr[m-1] < arr[m] > arr[m+1]):
                return m
            elif (arr[m-1] > arr[m]):
                r = m - 1
            else:
                l = m + 1

        # Pythonic O(n) time say
        # return arr.index(max(arr))
