"""
1513. Number of Substrings With Only 1s
https://leetcode.com/problems/number-of-substrings-with-only-1s/
"""

class Solution:
    def numSub(self, s: str) -> int:

        # Iteration
        # [1] split the string by 0s to get a list of 1's and '',
        # [2] Count the number of 1s in a run of 1st and add to result
        # [3] Return the number modulo (10**9 + 7)
        # Time and space complexity: O(n)

        # '111': 6 = 3 + 2 + 1 = 3 1's + 2 11's + 1 111
        # '1111': 10 = 4 + 3 + 2 + 1 = 4 1's + 3 11's + 2 111's + 1 1111s
        # length n(n+1)/2

        # Ex, "011001000111".split('0') -> ['', '11', '', '1', '', '', '111']


        ss_list = s.split('0')
        res = 0
        for ss in ss_list:
            if ss:
                res += len(ss) * (len(ss) + 1) // 2
        return res % (10**9 + 7)
