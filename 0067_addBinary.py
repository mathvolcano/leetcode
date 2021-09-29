"""
67. Add Binary
https://leetcode.com/problems/add-binary/
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # O(n + m) time an space.
        if a == '0': return b
        if b == '0': return a

        res = ''
        n_a, n_b = len(a) - 1, len(b) - 1
        carry = 0
        while n_a >= 0 or n_b >= 0:
            total = carry

            if n_a >= 0:
                total += int(a[n_a])
                n_a -= 1

            if n_b >= 0:
                total += int(b[n_b])
                n_b -= 1

            res = str(total % 2) + res
            carry = total // 2

        if carry:
            res = '1' + res
        return res
