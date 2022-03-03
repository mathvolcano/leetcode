"""
709. To Lower Case
https://leetcode.com/problems/to-lower-case/
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
    # O(n) time and O(1) space

    # If you want to use ASCII mathematical relationship
    # return "".join([chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s])

    # Brute force works
    # return ''.join([c.lower() for c in s])

    # Pythonic O(n) time and space
    # return s.lower()