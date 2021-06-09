"""
448. Find All Numbers Disappeared in an Array
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Modify in place
        # Idea: use the index to encode whether or not the value has appeared
        # But we want to be sure to not overwrite the value of the index encoded.
        # So we flip sign and us abs to recover value.
        for n in nums:
            i = abs(n) - 1
            nums[i] = -abs(nums[i])
        return [i+1 for i, v in enumerate(nums) if v > 0]


        # # O(n) extra space, O(n) runtime
        # from collections import defaultdict
        # d = defaultdict(int)
        # for v in nums:
        #     d[v] += 1
        # return [i for i in list(range(1, len(nums))) if d[i] == 0]

        # Pythonic - O(n) time & O(n) space
        # return list(set(range(1, len(nums)+1)) - set(nums))
