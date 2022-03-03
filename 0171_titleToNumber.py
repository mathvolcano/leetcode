"""
171. Excel Sheet Column Number
https://leetcode.com/problems/excel-sheet-column-number/
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        from functools import reduce
        return reduce(lambda res, c: res * 26 + ord(c) - ord('A') + 1, columnTitle, 0)