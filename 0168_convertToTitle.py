"""
168. Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        from string import ascii_uppercase
        lookup = dict(enumerate(ascii_uppercase, start=1))
        excel = ""
        while columnNumber > 0:
            lsd = columnNumber % 26
            lsd = 26 if lsd == 0 else lsd
            excel = lookup[lsd] + excel
            columnNumber -= lsd
            columnNumber //= 26
        return excel
