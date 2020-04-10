"""
645. Set Mismatch
https://leetcode.com/problems/set-mismatch/
"""


def findErrorNums(nums):
    hash_table = [0] * len(nums)
    for n in nums:
        hash_table[n - 1] += 1
    return [hash_table.index(2) + 1, hash_table.index(0) + 1]
