"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # BFS with sort
        # [0] Initialize result object res = [[]]
        # [1] sort nums O(nlg n) so that dupes are next to each other
        # [2] For each element of nums, check if it is in h
        # [3] if not a duplicate add to all arrays existing in res (not inplace)
        # [4] else, if it is add to only the previous subsets
        # [5] append to res
        # Complexity: n = len(nums)
        # Sort only O(n lg n)
        # Time: O(n * 2^n) because, worst case, number of subsets doubles at each call and we make n calls
        # Space: O(n * 2^n) worst & average cases to store doubling number of subsets, each subset storing
        # at most n elements.
        nums.sort()
        res, p = [[]], None # result, previous
        for i,v in enumerate(nums):
            vs, vl = [], [v] # v's Set, v's list
            if not p or (i>0 and v != nums[i-1]):
                for s in res:
                    vs.append(s + vl)
            else:
                for s in p:
                    vs.append(s + vl)
            p = vs
            res += vs
        return res


#         # Recursion
#         def helper(n, selected):
#             if n == len(nums):
#                 power_set.add(tuple(selected))
#                 return
#             helper(n+1, selected)
#             new_list = list(selected) + [nums[n]]
#             new_list.sort()
#             helper(n+1, new_list)

#         power_set = set()
#         helper(0, tuple())
#         power_set = list(power_set)
#         power_set.sort()
#         return power_set