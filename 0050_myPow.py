"""
50. Pow(x, n)
https://leetcode.com/problems/powx-n/
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Bitwise exponentiation approach
        # result = 1
        # power = n
        # if n < 0:
        #     power, x = -power, 1./x
        # while power:
        #     if power & 1:
        #         result *= x
        #     x *= x
        #     power = power >>1
        # return result


        # Recursion of Binary exponentiate until n powers are computed.
        # Time complexity: log_2(n) calls so time complexity is O(log n)
        # Space complexity is O(log n) because of the recursive calls
        if n < 0:
            n, x = -n, 1./x

        def helper(x, n):
            if x == 1 or n == 0: return 1
            if n == 1: return x
            temp = helper(x, n // 2)
            if n % 2 == 0:
                return temp ** 2
            else:
                return (temp ** 2) * x

        return helper(x, n)

