"""
18. 4Sum
https://leetcode.com/problems/4sum/
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        # 2 pointer
        # [1] sort arr
        # [2] for i in range(n)
        # [3] skip duplicates if i > 0 and ai == arr[i-1]: continue
        # [4] iterate through an inner loop, for j in range(i, n-2):
        # [5] 2 pointer
        # Time: O(n^3) needed for 3 loops
        # Space: O(n) needed for sorting, and O(1) for additional variables.
        # If we can print the result no additional storage needed. Otherwise, need an additional O(n)
        # for building result.
        nums.sort()
        n = len(nums)
        for i in range(n):
            # skip same element to avoid duplicate quadruplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ai = nums[i]
            for j in range(i+1, n-2):
                aj = nums[j]
                # skip same element to avoid duplicate quadruplets
                if j > i+1 and nums[j] == nums[j - 1]:
                    continue
                l, r = j+1, n-1
                while l < r:
                    al, ar = nums[l], nums[r]
                    s = ai + aj + al + ar
                    d = target - s
                    if s == target:
                        res.append([ai, aj, al, ar])
                        # Skip duplicates
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res
