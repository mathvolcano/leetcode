"""
46. Permutations
https://leetcode.com/problems/permutations/
"""


def permute(nums):
    if len(nums) == 1: return [nums]
    if len(nums) == 2: return [[nums[0], nums[1]],
                               [nums[1], nums[0]]]

    # Factory method
    # import itertools
    # return list(itertools.permutations(nums))
    results = []
    for i in range(len(nums)):
        n = nums[i]
        exclude_n = nums[:i] + nums[i+1:]
        non_n_perm = permute(exclude_n)
        perms = [[n] + p for p in non_n_perm]
        results = results + perms
    return results




nums = [1,2,3]
print(permute(nums))