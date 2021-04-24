"""
1228. Missing Number In Arithmetic Progression
https://leetcode.com/problems/missing-number-in-arithmetic-progression/
"""

class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        # Find correct delta
        diff1 = arr[1] - arr[0]
        diff2 = arr[2] - arr[1]
        if diff1 == diff2:
            delta = diff1
        elif abs(diff1) > abs(diff2):
            delta = diff2
        else:
            delta = diff1

        # Exception
        if delta == 0: return arr[0]

        # Find missing value
        correct = delta + arr[0]
        for _, v in enumerate(arr[1:], start=1):
            if v != correct:
                return correct
            else:
                correct += delta
