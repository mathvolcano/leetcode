"""
78. Subsets
https://leetcode.com/problems/subsets/
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # Time – Recursion C(n) = 2*C(n-1) gives O(2^n). O(n) time within a call and O(2^n)
        # calls yields O(n * 2^n)
        # Space – O(n* 2^n) because there are O(2^n) subsets and average size O(n/2).
        def helper(n, selected):
            if n == len(nums):
                power_set.append(selected)
                return
            helper(n+1, selected)
            helper(n+1, selected + [nums[n]])

        power_set = []
        helper(0, [])
        return power_set

        # Nonrecursive - bijections of subsets with len(nums) bit-strings.
        # Space – O(n* 2^n) because there are O(2^n) subsets and average size O(n/2).
        # But if you want to print them then space is only O(n)
        # power_set = []
        # for i in range(1 << len(nums)):
        #     bit_arr = i
        #     subset = []
        #     while bit_arr:
        #         subset.append(int(math.log2(bit_arr & ~(bit_arr - 1))))
        #         bit_arr &= bit_arr - 1
        #     power_set.append([nums[s] for s in subset])
        # return power_set
