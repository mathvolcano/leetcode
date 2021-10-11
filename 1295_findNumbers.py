"""
1295. Find Numbers with Even Number of Digits
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # 1 Define a n_digits function that divides the number by 10
        # 2 Iterate through the array and increment result var if the number of digits is even
        # O(len(nums) * m) time complexity where m is the max number of digits of the longest integer
        # in nums. O(1) space.
        def n_digits(n):
            cur = 0
            while n > 0:
                cur += 1
                n //= 10
            return cur

        res = 0
        for n in nums:
            if n_digits(n) % 2 == 0:
                res += 1

            # Pythonic – don't need n_digits
            # if len(str(n)) % 2 == 0:
            #     res += 1
        return res
