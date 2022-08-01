"""
46. Permutations
https://leetcode.com/problems/permutations/
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # [1] Given all the permutation of a subarray, perms_sub, add the next element after the
        # perms_sub to sub to get a new all the new permutations that include the next element
        # e.g., perms_sub + [perms_sub + [current]]
        # [2] Perform a DFS iterating through nums
        # O(n!) time and space.

        # def helper(arr, current, permutations):
        #     if not len(arr) and len(current):
        #         permutations.append(current)
        #     else:
        #         for i in range(len(arr)):
        #             newArr = arr[:i] + arr[i+1:]
        #             newCurr = current + [arr[i]]
        #             helper(arr, newCurr, permutations)
        # result = []
        # helper(nums, [], result)
        # return result

        # [0] Initialize result object, res = []
        # [1] Iterate through each value of nums and, for every element already in result, insert
        # the value into every position
        # Complexity: n = len(nums)
        # Time: O(n * n!) because each element of result has length at most n for inserting elements
        # and the number of permutations is order n!.
        # Space: O(n * n!) because each element of result has length n and the number of
        # permutations is order of n!.
        res = []
        for n in nums:
            if len(res) == 0: res.append([n])
            else:
                lvl = []
                for i, e in enumerate(res):
                    for j in range(len(e)+1):
                        k = e.copy()
                        k.insert(j, n)
                        lvl.append(k)
                res = lvl
        return res





    # # Base Case
    # if len(nums) == 1: return [nums]
    # if len(nums) == 2: return [[nums[0], nums[1]],
    #                            [nums[1], nums[0]]]

    # Factory method
    # import itertools
    # return list(itertools.permutations(nums))
    # Recursion
    results = []
    for i in range(len(nums)):
        n = nums[i]
        exclude_n = nums[:i] + nums[i+1:]
        non_n_perm = permute(exclude_n)
        perms = [[n] + p for p in non_n_perm]
        results = results + perms
    return results
