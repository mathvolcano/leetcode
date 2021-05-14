"""
15. 3Sum
https://leetcode.com/problems/3sum/
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # See https://medium.com/swlh/crack-leetcode-15-3sum-b0dfd80c3550
        # for other solutions

        # [1] Sort nums
        # [2] For a given value in nums create a hash_map and perform 2-sum
        # [3] nums found and append to a solution set
        # [4] Remove duplicates from set
        # O(n^2) time for double for loop (reduce from O(n^3) using the hash_set)
        # O(n^2) space for the hash_set and ans worst case

        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            hash_set = set()
            vi = nums[i]
            target = - vi
            for j in range(i+1, n):
                vj = nums[j]
                diff = target - vj
                if diff not in hash_set:
                    hash_set.add(vj)
                else:
                    triplet = [vi, vj, diff]
                    triplet.sort()
                    ans.append(tuple(triplet))
        uniques = list(set(ans))
        return [list(x) for x in uniques]

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
