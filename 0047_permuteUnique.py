"""
47. Permutations II
https://leetcode.com/problems/permutations-ii/
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # [1] Given all the permutation of a subarray, perms_sub, add the next element after the
        # perms_sub to sub to get a new all the new permutations that include the next element
        # e.g., perms_sub + [perms_sub + [current]]
        # [2] Perform a DFS iterating through nums
        # O(n!) time and space.
        # Only difference between this and 46 is that we cast list to tuple and check for uniqueness with a set (lists are not hashable)
        def helper(arr, current, result):
            # Terminating case
            if len(arr) == 0 and len(current) > 0:
                result.add(tuple(current))
            else:
                for i in range(len(arr)):
                    newArr = arr[:i] + arr[i+1:]
                    newCur = current + [arr[i]]
                    helper(newArr, newCur, result)

            return -1

        result = set()
        helper(nums, [], result)
        return list(result)
