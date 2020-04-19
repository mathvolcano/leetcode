"""
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/
"""

def findMaxLength(nums) -> int:
    if len(nums) <= 1: return 0

    hash_table = {0: -1}
    max_len, count = 0, 0
    for i, n in enumerate(nums):
        count += 1 if n == 1 else -1

        if count in hash_table:
            max_len = max(max_len, i - hash_table[count])
        else:
            hash_table[count] = i

    return max_len
