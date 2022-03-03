"""
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Binary search
        # [1] on the value the range [1,n], calculate the mid, (n) //2
        # [2] count the number of elements in nums less than m, if more elements are smaller than they are large then decrease r. Else increase l
        # [3] Repeat until search ends. Return l
        # O(n) time for search O(1) space
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            m = (l + r) // 2
            n_elems = len([x for x in nums if x <= m])
            if n_elems > m:
                r = m
            else:
                l = m + 1
        return l

    # Use approach from linked list
    # O(n) time and O(1) space
    #         slow = fast = 0
    #         while True:
    #             fast = nums[nums[fast]]
    #             slow = nums[slow]
    #             # Always terminates because we have duplicates
    #             if fast == slow:
    #                 break

    #         dup = 0
    #         while dup != slow:
    #             dup = nums[dup]
    #             slow = nums[slow]
    #         return dup


    # # Hash table O(n^2) time and O(n) space for table
    # cache = {}
    # for n in nums:
    #     cache[n] = cache.get(n, 0) + 1
    # return [k for k,v in cache.items() if v == 2][0]

