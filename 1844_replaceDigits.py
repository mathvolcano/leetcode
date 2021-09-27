"""
1844. Replace All Digits with Characters
https://leetcode.com/problems/replace-all-digits-with-characters/
"""

class Solution:
    def replaceDigits(self, s: str) -> str:

        # 1 Initialize result string: res = ''
        # 2. Iterate through the string array
        # 2a. If the char is a letter append to result string
        # 2b. Else cast the char to an integer and add shift to previous alpha char
        #     and convert to a character. Append result to res string
        # O(s) time and O(s) space

        res = ''
        for i, v in enumerate(s):
            if 96 < ord(v) < 123:
                res = res + v
            else:
                res = res + chr(ord(s[i-1]) + int(v))
        return res
