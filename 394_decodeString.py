"""
394. Decode String
https://leetcode.com/problems/decode-string/
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # Use a stack to hold bracketed values
        # Append results to a string

        # O(n) time complexity
        # Space complexity depends on size of int
        stack = []
        num = 0
        substr = ''
        for _, c in enumerate(s):
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                stack.append(substr)
                stack.append(num)
                substr, num = '', 0  # Reset
            elif c.isalpha():
                substr += c
            elif c == ']':
                pre_num = stack.pop()
                pre_str = stack.pop()
                substr = pre_str + pre_num * substr
        return substr
