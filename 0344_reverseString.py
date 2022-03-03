"""
344. Reverse String
https://leetcode.com/problems/reverse-string/
"""

class Solution:
    def reverseString(self, s: List[str], start=0) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        if len(s[start:l-start]) <= 1:
            return

        end = l - start - 1
        s[start], s[end] = s[end], s[start]
        self.reverseString(s, start+1)
