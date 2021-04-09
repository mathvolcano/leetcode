"""
https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
1287. Element Appearing More Than 25% In Sorted Array
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        # Perform a binary search to count the number of occurrences of a value.
        # If the value appears more than 25% then return it.
        # If not, then check the next value
        # O(log n) time, O(1) space

        # Trivial
        n = len(arr)
        if n == 0: return arr
        if n <= 3: return arr[0]

        ind = 0
        while ind < n:
            this_num = arr[ind]
            next_ind = self.binary_search(arr, this_num)
            if (next_ind - ind) > n // 4:
                return this_num
            ind = next_ind
        return -1

    def binary_search(self, arr, num):
        """Get the index of the next element to search that's at least as large as num."""
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] <= num:
                l = m + 1
            else:
                r = m
        return l


        # # Brute force O(n)
        # from collections import Counter
        # counts = dict(Counter(arr))
        # total = sum(counts[c] for c in counts)
        # return max(c for c in counts if counts[c] > total // 4)
