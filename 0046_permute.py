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

        def helper(arr, current, permutations):
            if not len(arr) and len(current):
                permutations.append(current)
            else:
                for i in range(len(arr)):
                    newArr = arr[:i] + arr[i+1:]
                    newCurr = current + [arr[i]]
                    helper(newArr, newCurr, permutations)

        result = []
        helper(nums, [], result)
        return result





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
