"""
258. Add Digits
https://leetcode.com/problems/add-digits/
"""
class Solution:
    def addDigits(self, num: int) -> int:

        # "Casting out the 9s"
        # [1] Decimal expand num = d0 + d1*10 + d2*100
        # [2] Rewrite as expansion of 9s
        #.    num = (d0 + ... + dk) + 9*(d1*1 + d2*11 + ... + dk*111...1)
        # this gives us the formula
        # O(1) time & space
        if num == 0: return 0
        if num % 9 == 0: return 9
        return num % 9

        # Naive
        # Time: O(log num) & space O(1)
        def helper(n):
            res = 0
            while n:
                res += n % 10
                n //= 10
            return res

        while num >= 10:
            num = helper(num)
        return num
