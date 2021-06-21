"""
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # O(numRows *numRows) space, O(numRows ^2) time.
        res = [[1]]
        row, i = [1], 1
        while numRows > i:
            row, i = self.helper(row, i)
            res.append(row)
        return res

    def helper(self, r, idx):
        """Get next row of Pascal's Triangle."""
        r = [r[i] + r[i - 1] for i in range(1,len(r))]
        r = [1] + r + [1]
        return r, idx + 1
