"""
529. Minesweeper
https://leetcode.com/problems/minesweeper/
"""

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        # Recursion
        # [0] define all directions
        # [1] if mine is reveled update 'M' -> 'X'
        # [2] if 'E' with adjacent mines count adjacent mines and return number '1' to '8'.
        # Do not recurse
        # [3] if 'E' revealed change to 'B' if no mines and recurse on all adjacent unrevealed squares
        # [3] return board
        # Time complexity is O(mn) because we may have to check up to all entries
        # Space complexity O(mn) because of stack memory for recursion

        m, n = len(board), len(board[0])
        x, y = click
        directions = ((-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1))
        if 0 <= x < m and 0 <= y < n:
            if board[x][y] == 'M':
                board[x][y] = 'X'
            elif board[x][y] == 'E':
                mines = sum([board[x + r][y + c] == 'M' for r, c in directions if 0 <= x + r < m and 0 <= y + c < n])
                board[x][y] = str(mines) if mines else 'B'
                if not mines:
                    for r, c in directions:
                        self.updateBoard(board, [x + r, y + c])
        return board
