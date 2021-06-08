"""
16. 3Sum Closest
https://leetcode.com/problems/3sum-closest/
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # 2-pointer solution
        # [1] sort nums
        # [2] For each index in nums perform a 2-pointer search to find smallest target
        # [2a] set left l and right r pointers to the endpoints
        # [2b] compute sum of the three values num
        n = len(nums)
        nums.sort()
        ans = sum(nums[:3])
        min_diff = abs(ans - target)
        for i in range(n-2):
            l = i + 1
            r = n - 1
            while l < r:
                tot = nums[i] + nums[l] + nums[r]
                diff = tot - target

                # Update ans
                abs_diff = abs(diff)
                if abs_diff < min_diff:
                    ans = tot
                    min_diff = abs_diff

                # Update pointers
                if diff == 0:
                    return tot
                elif diff > 0:
                    r -= 1
                elif diff < 0:
                    l += 1
        return ans

        # Brute force
        # [1] Get all triplets of values in nums
        # [2] Compute their sums
        # [3] Return min sum
        # min_diff = float('inf')
        # ans = float('inf')
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             val = nums[i] + nums[j] + nums[k]
        #             diff = target - val
        #             abs_diff = abs(diff)
        #             if abs_diff < min_diff:
        #                 ans = diff
        # return ans
