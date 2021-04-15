"""
989. Add to Array-Form of Integer
https://leetcode.com/problems/add-to-array-form-of-integer/
"""

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:

        # Convert num to an integer, add n+k, convert back to int-arry.
        # O(n) time, O(n+k) space
        n, power = 0, 1
        while num:
            n += num.pop() * power
            power *= 10

        res = n+k
        return [int(x) for x in str(res)]

        # Converting k to integer array and then adding
#         karr = [int(x) for x in list(str(k))]

#         # Add array-form integers by carrying
#         # O(n + k) time and O(n + k) space
#         if len(num) < len(karr):
#             num, karr = karr, num
#         n, carry = len(karr), 0
#         res = []
#         for i in range(n):
#             n_val, k_val = num[-i-1], karr[-i-1]
#             val = n_val + k_val + carry
#             carry = 0 if val <= 9 else int(str(val)[:-1])
#             res.insert(0, val % 10)

#         # Add rest of the longer sequence
#         for j in range(i+1, len(num)):
#             val = num[-j-1] + carry

#             carry = 0 if val <= 9 else int(str(val)[:-1])
#             res.insert(0, val % 10)

#         # Add carry
#         if carry:
#             res.insert(0, carry % 10)

#         return res
