"""
202. Happy Number
https://leetcode.com/problems/happy-number/
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        # Fast & Slow pointer
        # [1] Define helper function, ss, as sum of digits squared
        #. a. while val > 0
        #  b. get one
        # [2] initialize 2 values, s, f = n, n (slow & fast)
        # [3] while f != 1 and ss(f) != 1, update s = ss(s) and f = ss(ss(s))
        # [4] If f == s: return False, else break & return True
        # Complexity:
        # Time: O(log(n))
        # If n < 1000, then we reach the cycle in at most 1001 steps
        # Let m = number of digits of n And n2 the next num in the sequence
        # then m = log(n) and n2 <= 81m = 82 log(n) => time is O(log(n)).
        # Space: O(1)
        def ss(v):
            # sum of digits squared
            res = 0
            while v:
                res += (v % 10)**2
                v //= 10
            return res

        s, f = n, n
        while True:
            s, f = ss(s), ss(ss(f))
            if f == s:
                break
        return s == 1

        # Hashset
        # [1] Define a helper sum of digits squared function
        # [2] iterate the sequence of n & store values in a hashset
        # [3] if n hits the hashset then break and return if n == 1
        # O(n) space to store hashset & O(n) time
        # def sum_of_squared_digits(k):
#             val = 0
#             while k:
#                 val += (k % 10) ** 2
#                 k //= 10
#             return val

#         visited = set([1,n])
#         while n:
#             n = sum_of_squared_digits(n)
#             if n in visited:
#                 break
#             else:
#                 visited.add(n)
#         return n == 1
