"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Can we use binary search?
        # nums1 = [1,2,9,10], nums2 = [-1, 0 ,0, 2]
        #partition them nums1 = [1,2|9,10], nums2 = [-1, 0|0, 2] into parts l1, r1, l2, r2
        # corresponds with partitioning merged list [-1, 0 | 0, 1,2,2|,9, 10]
        # so we'd want to decrease partition for nums and increase for r2
        # Can only merge nums if max(l1) <= min(r1) and max(l2) <= min(r1)
        # Otherwise we update the endpoint of the BS to be mid of the nums 1 if max(l1) >= min(r2)
        # https://www.youtube.com/watch?v=lLFDQCDzfpI

        def get_min(nums, p):
            """Given p pointer get the max of a sorted array."""
            return float('inf') if p == len(nums) else nums[p]

        def get_max(nums, p):
            """Given p pointer get the min of a sorted array."""
            return -float('inf') if p == 0 else nums[p-1]

        def median(sorted_nums):
            n = len(sorted_nums)
            m = n // 2
            return sorted_nums[m] if (n % 2 == 1) else (sorted_nums[m] + sorted_nums[m-1]) / 2


        n1, n2 = len(nums1), len(nums2)

        # Make nums1 at least as short as nums2
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        n = n1 + n2
        print('n', n)

        if n == 0:
            return float('inf')
        elif n1 == 0:
            return median(nums2)

        s, b = 0, n1 # smallest and biggest
        while s <= b:
            print('s', s, 'b', b)
            m1 = (s + b) // 2
            m2 = (n + 1) // 2 - m1
            print('m1', m1, 'm2', m2)
            l1, r1 = get_max(nums1, m1), get_min(nums1, m1)
            print('l1', l1, 'r1', r1)
            l2, r2 = get_max(nums2, m2), get_min(nums2, m2)
            print('l2', l2, 'r2', r2)

            if (l1 <= r2) and (l2 <= r1):  # Found median
                print('found median')
                if n % 2 == 0:  # even
                    # print()
                    return (max(l1, l2) + (min(r1, r2))) / 2
                else:  # odd
                    return max(l1, l2)

            # Binary search update pointer
            if l1 > r2:
                b = m1 - 1
            else:
                s = m1 + 1
        return (nums1[m1-1] + nums2[m2]) / 2



        # [1]. Do a linear scan of nums 1 and nums2 to count length n1 and n2
        # [2]. Use 2 pointers and count off nums1 and nums2.
        # [3]. Stop when we reach median if n1 + n2 % 2 == 1 or get middle 2 elements
        # and averaage.
        # This has time complexity O(n + m), O(1) additional space complexity

        # Brute Force – Merge the lists together and sort O(n log n)
        # Return the median
        # Can we do better?
        # full_nums = nums1 + nums2
        # full_nums.sort()
        # n = len(full_nums)
        # print(full_nums)
        # m = (n // 2)  # mid
        # print(m)
        # if n % 2 == 1:
        #     return full_nums[m]
        # else:
        #     return (full_nums[m] + full_nums[m -1]) / 2
