"""
1387. Sort Integers by The Power Value
https://leetcode.com/problems/sort-integers-by-the-power-value/
"""

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        # 1. Define a helper to count the power of an integer
        # 2. Calculate power of each number between lo and hi
        # 3. Sort the powers in ascending order
        # 4. Return the k-th integer.

        # Time complexity: O(n log n) for sort, O(hi-lo) for space

        # Iterative
        def power(n):
            if n == 1:
                return 1
            count = 0
            while n != 1:
                if n % 2 == 0:
                    n /= 2
                    count += 1
                else:
                    n = 3 * n + 1
                    count += 1
            return count

        # Recurseive
        # def power(n, powers=1):
        # if n == 1:
        #     return powers
        # if n % 2 == 0:
        #     n /= 2
        # else:
        #     n = 3 * n + 1
        # powers += 1
        # return power(n, powers)


        from collections import defaultdict
        d = defaultdict(list)
        res = []
        for i in range(lo, hi+1):
            d[power(i)].append(i)
        for keys in sorted(d.keys()):
            res.extend(d[keys])
        return res[k-1]