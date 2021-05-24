"""
51. N-Queens
https://leetcode.com/problems/n-queens/
"""

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Recursion
        # Note we can describe a board as an array whose index corresponds to rows of the board
        # [1] If an array is of length n then append to our results because the board is filled
        # [2] For a given array add all columns to the results which do not lead to a
        # row or diagonal conflict
        # [3] Recurse on the resulting board
        # [4] Post-process board to satisfy board display
        # Time & space complexity – no one knows, but at worse O(n!)

        # From EPI
        def n_queens(row, result):
            if row == n:  # all queens placed
                result.append(col_placement.copy())
                return
            for col in range(n):
                # Check for row and diagonal conflicts
                if all(abs(c-col) not in (0, row - i)
                       for i, c in enumerate(col_placement[:row])
                       ):
                    col_placement[row] = col
                    n_queens(row + 1, result)

        result = []
        col_placement = [0] * n
        n_queens(0, result)

        # Transform result to board
        print('result before', result)
        for i, b in enumerate(result):
            new_b = []
            for r in b:
                new_r = ['.'] * n
                new_r[r] = 'Q'
                new_b.append(''.join(new_r))
            result[i] = new_b
        print('result after', result)

        return result
