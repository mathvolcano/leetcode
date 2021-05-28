"""
477. Total Hamming Distance
https://leetcode.com/problems/total-hamming-distance/
"""

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        # [1] For each number count the 0s and 1s
        # [2] track the count of 0s and 1s for each bit in a hash_table
        # [3] sum the product of values
        # Ex 1, nums = [4,14,2]
        # bits = [[0,0],....,[0,0], [2,1], [1,2], [1,2], [3,0]]
        # result = 2*1 + 1*2 + 1*2 = 6
        bits = [[0,0] for _ in range(32)]
        for n in nums:
            for bit in bits:
                bit[n & 1] += 1
                n >>= 1
        return sum([x*y for x,y in bits])

        # Brute Force
        # import itertools
        # res = 0
        # for x, y in itertools.combinations(nums, 2):
        #     res += bin(x^y).count('1')
        # return res
