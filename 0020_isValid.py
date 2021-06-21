"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(' ', '')  # Remove whitespace
        parentheses_pairs = ['()', '[]', '{}']
        is_valid = True
        l_previous = len(s)
        while l_previous > 0:
            for parenth in parentheses_pairs:
                if parenth in s:
                    s = s.replace(parenth, '')
            l_new = len(s)
            if l_previous == l_new:
                is_valid = False
                break
            l_previous = l_new
        return is_valid
