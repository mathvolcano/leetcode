"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""

class Solution:

    # Recursion & Backtracking
    # [1] check if the current str is terminal and has equal number of open and closed parentheses equal to max.
    # if so append to a result variable
    # [2] If the number of open parenthesis is less than the max in the current string then add '(' to it and recurse.
    # [3] If the number of closed parenthesis is less than the max in the current string then add ')' to it and recurse.
    # Note if we reach an invalid parenthesis this way then we discard it.
    # Time complexity: Catalan numbers requires O(n * 4^n/ n^(3/2)) = O(4^n / n^.5)
    # Master theorm implies T(n) = 2 T(n/2) =
    # Space complexity: O(4^n / n^.5) for the n recursive call stack

    # Example n = 3
    # Pass 1: array=[], cur = '(', 1, 0, 3
    # Pass 2: array=[], cur = '((', 2, 0, 3
    # Pass 3: array=[], cur = '(((', 3, 0, 3
    # Pass 4: array=[], cur = '((()', 3, 1, 3
    # Pass 5: array=[], cur = '((())', 3, 2, 3
    # Pass 6: array=[], cur = '((()))', 3, 3, 3

    # Pass 7: array=['((()))'], cur = '(()', 2, 1, 3
    # Pass 8: array=['((()))'], cur = '(()(', 3, 1, 3
    # Pass 9: array=['((()))'], cur = '(()()', 3, 2, 3
    # Pass 10: array=['((()))'], cur = '(()())', 3, 3, 3
    # Pass 11: array=['((()))', '(()())'], cur = '(())', 2, 2, 3
    # Pass 12: array=['((()))', '(()())'], cur = '(())(', 3, 2, 3
    # Pass 13: array=['((()))', '(()())'], cur = '(())()', 3, 3, 3
    # Pass 14: array=['((()))', '(()())', '(())()'], cur = '()(', 2, 1, 3
    # Pass 15: array=['((()))', '(()())', '(())()'], cur = '()((', 3, 1, 3
    # Pass 16: array=['((()))', '(()())', '(())()'], cur = '()(()', 3, 2, 3
    # Pass 17: array=['((()))', '(()())', '(())()'], cur = '()(())', 3, 3, 3
    # Pass 18: array=['((()))', '(()())', '(())()', '()(())'], cur = '()()', 2, 2, 3
    # Pass 19: array=['((()))', '(()())', '(())()', '()(())'], cur = '()()(', 3, 2, 3
    # Pass 20: array=['((()))', '(()())', '(())()', '()(())'], cur = '()()()', 3, 3, 3
    # return ['((()))', '(()())', '(())()', '()(())', '()()()']



    def backtrack(self, array, current_str, n_open, n_closed, n_max):
        if n_open == n_closed == n_max:
            array.append(current_str)
            return

            # backtrack
        if n_open < n_max:
            self.backtrack(array, current_str + '(', n_open + 1, n_closed, n_max)
        if n_closed < n_open:
            self.backtrack(array, current_str + ')', n_open, n_closed + 1, n_max)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.backtrack(res, '', 0, 0, n)
        return res
