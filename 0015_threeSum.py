"""
15. 3Sum
https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    # [1] Sort
    # [2] Perform sorted 2-sum with a 2 pointer approach
    # [3] Iterate through enumerate(arr)
    # [4] if arr[i] == arr[i-1] then continue
    # [5] Else set l, r = i+1, len(arr) -1 and while l < r
    # [6] get sum s = arr[i] + arr[l] + arr[r] and if > 0 then decrement r, if < 0 increment l
    # else append triplet to result and skip duplicates of l and r before going to next
    # Complexity n = len(arr), then time: O(nlogn + n**2) = O(n^2).
    # O(n) space depending on the sorting algorithm
    res = []
    nums.sort()
    for i, ai in enumerate(nums):
        if i > 0 and ai == nums[i-1]:
            continue
        l, r = i+1, len(nums) - 1
        while l < r:
            al, ar = nums[l], nums[r]
            s = ai + al + ar
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([ai, al, ar])
                # Skip duplicates
                while l < r and al == nums[l+1]:
                    l += 1
                while l < r and ar == nums[r-1]:
                    r -= 1
                l += 1; r -= 1
    return res

        # See https://medium.com/swlh/crack-leetcode-15-3sum-b0dfd80c3550
        # for other solutions

        # [1] Sort nums
        # [2] For a given value in nums create a hash_map and perform 2-sum
        # [3] nums found and append to a solution set
        # [4] Remove duplicates from set
        # O(n^2) time for double for loop (reduce from O(n^3) using the hash_set)
        # O(n^2) space for the hash_set and ans worst case

        # n = len(nums)
        # nums.sort()
        # ans = []
        #
        # for i in range(n):
        #     hash_set = set()
        #     vi = nums[i]
        #     target = - vi
        #     for j in range(i+1, n):
        #         vj = nums[j]
        #         diff = target - vj
        #         if diff not in hash_set:
        #             hash_set.add(vj)
        #         else:
        #             triplet = [vi, vj, diff]
        #             triplet.sort()
        #             ans.append(tuple(triplet))
        # uniques = list(set(ans))
        # return [list(x) for x in uniques]

        # Brute Force O(n^3) time and space
        # n = len(nums)
        # res = set()
        # for i in range(n):
        #     for j in range(0, i):
        #         for k in range(0, j):
        #             l = [nums[i], nums[j], nums[k]]
        #             l.sort()
        #             v = sum(l)
        #             if v == 0:
        #                 res.add(tuple(l))
        # return list(list(v) for v in res)
