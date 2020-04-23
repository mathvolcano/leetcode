"""
https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3306/
"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Get dimensions and check trivial case
        dim = binaryMatrix.dimensions()
        n_rows, n_cols = dim
        if (n_rows == 0) or (n_cols == 0): return -1

        leftmost_1_col = -1
        r, c = 0, n_cols - 1
        while (r < n_rows) and (c >= 0):
            if binaryMatrix.get(r, c) == 1:
                leftmost_1_col = c
                c -= 1
            else:
                r += 1

        return leftmost_1_col
