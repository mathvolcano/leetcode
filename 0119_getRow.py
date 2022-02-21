"""
119. Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # O(row) space, O(n^2) time.
        base = {0: [1], 1: [1, 1]}
        if rowIndex in base: return base[rowIndex]

        row, i = [1, 2, 1], 2
        while rowIndex > i:
            row, i = self.helper(row, i)
        return row

    def helper(self, r, idx):
        """Get next row of Pascal's Triangle."""
        r = [r[i] + r[i - 1] for i in range(1,len(r))]
        r = [1] + r + [1]
        return r, idx + 1
