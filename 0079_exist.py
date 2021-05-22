"""
79. Word Search
https://leetcode.com/problems/word-search/
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # DFS
        # [1] If no word then terminate success. Iterate through the board
        # [2] If search is invalid or board[r][c] does not match next letter in word then False
        # [3] else the search is valid, pop the first letter of word, append [r,c] to path
        # compute neighbors. If neighbors not in visited then search
        # [4] Pop stack
        # Time complexity is O(m^2n^2) worst case and space complexity is O(mn) worst case
        if not board or not board[0] or not word: return False

        self.m, self.n = len(board), len(board[0])
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(board, r, c, word, visited):
            if not word: return True  # Success termination

            # Invalid r & c or don't have match
            invalid = not (0 <= r < self.m) or not (0 <= c < self.n)
            if invalid or word[0] != board[r][c] or [r, c] in visited:
                return False

            # We have match
            visited.append([r,c])
            nxt = (
                    dfs(board, r - 1, c, word[1:], visited) or \
                    dfs(board, r + 1, c, word[1:], visited) or \
                    dfs(board, r, c + 1, word[1:], visited) or \
                    dfs(board, r, c - 1, word[1:], visited)
            )
            if not nxt: visited.pop()  # Pop stack
            return nxt


        for r in range(self.m):
            for c in range(self.n):
                if dfs(board, r, c, word, []): return True
        return False