"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""

class Solution:

    def backtrack(self, array, current_str, n_open, n_closed, n_max):
        if len(current_str) == 2 * n_max:
            array.append(current_str)
            return

            # backtrack
        if n_open < n_max:
            self.backtrack(array, current_str + '(', n_open + 1, n_closed, n_max)
        if n_closed < n_open:
            self.backtrack(array, current_str + ')', n_open, n_closed + 1, n_max)

    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtrack(result, '', 0, 0, n)
        return result
