"""
137. Single Number II
https://leetcode.com/problems/single-number-ii/
"""


def singleNumber(nums):

    # brute force linear time with memory
    from collections import Counter
    hash_table = Counter(nums)
    for x in hash_table:
        if hash_table[x] == 1:
            return x

    # Without extra memory - bit count
    # http://traceformula.blogspot.com/2015/08/single-number-ii-how-to-come-up-with.html
    h, l = 0, 0
    for n in nums:
        h = l & (h ^ n)
        l = h | (l ^ n)
    return l