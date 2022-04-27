"""
697. Degree of an Array
https://leetcode.com/problems/degree-of-an-array/
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # Hash tables, brute force
        # [0] create hash tables of the left index, right index, and counts of each value in nums
        # [1] Iterate i,v through enumerate(nums)
        #. a. if v not in left then left[v] = i
        #. b. increase right[v] = i
        #. c. increase counts
        # [2] Initialize result variable, res = len(nums) and count the degree of nums
        # [3] Iterate through counts, if value is the mx then update res as the min of res and length of the subarray right[k] - left[k] + 1
        # O(n) time and space
        left, right, count = {}, {}, {}
        for i,v in enumerate(nums):
            if v not in left: left[v] = i
            right[v] = i
            count[v] = count.get(v,0) + 1

        res = len(nums)
        degree = max(count.values())
        for k,v in count.items():
            if v == degree:
                res = min(res, right[k] - left[k] + 1)
        return res
