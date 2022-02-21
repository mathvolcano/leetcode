"""
970. Powerful Integers
https://leetcode.com/problems/powerful-integers/
"""

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        # [1] For each x and y create a hash set to store all powers of x up to bound
        # [2] Use the hash sets to compute the cross sums x^i and y^j
        # [3] Return distinct sums.
        # Time complexity O(log(bound)/log(x) * log(bound)/log(x))
        # Space complexity O(log(bound)/log(x) * log(bound)/log(x))
        # Because we need to compute all powers for both x and y and take and store cross operations.

        # x hash set
        x_set = set()
        xpow = x
        if xpow == 1:
            x_set.add(xpow)
        else:
            while xpow <= bound:
                x_set.add(xpow)
                xpow *= x
        x_set.add(1)

        # y hash set
        y_set = set()
        ypow = y
        if ypow == 1:
            y_set.add(ypow)
        else:
            while ypow <= bound:
                y_set.add(ypow)
                ypow *= y
        y_set.add(1)

        new_set = set(x+y for x in x_set for y in y_set if x+y <= bound)
        return list(new_set)
