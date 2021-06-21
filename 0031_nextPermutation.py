"""
31. Next Permutation
https://leetcode.com/problems/next-permutation/
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [1] Base/trivial cases
        # [2] 2 pointer solution. Swap adjacent pairs of numbers starting from the right side
        # until we have a larger results.
        # Example: [1,5,8,4,7,6,5,1] -> [1,5,8,5,1,4,6,7]
        n = len(nums)

        # [1] Find the earliest number that is less than the number after it
        # Selects i =3 or nums[3] = 4 in [1,5,8,4,7,6,5,1]
        i = n - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        print('i', i)

        # [2] Find the smallest number after i that is bigger than it and swap the numbers
        # [1,5,8,4,7,6,5,1] -> [1,5,8,5,7,6,4,1]
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        print('nums after [2]', nums)

        # [3] order the numbers to the right of i in ascending order by transposition
        # e.g., bubble sort.
        # [1,5,8,5,7,6,4,1] ->[1,5,8,5,1,4,6,7]
        k = n - 1
        while i < k:
            i += 1
            nums[i], nums[k] = nums[k], nums[i]
            k -= 1
        # Bubble sort is O(n^2) which is worse case time complexity. O(1) additional space

#         # Brute Force  – write all permutations, sorted, then get next one
#         # after the nums
#         import itertools
#         n = len(nums)
#         perms = list(itertools.permutations(nums, n))
#         perms.sort()
#         print(perms)

#         for i, p in enumerate(perms):
#             if nums == list(p):
#                 break
#         nums = perms[i+1] if (i < n-1) else perms[0]
