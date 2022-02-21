"""
136. Single Number
https://leetcode.com/problems/single-number/
"""


def singleNumber(nums):
    result = 0
    for n in nums:
        result ^= n
    return result
