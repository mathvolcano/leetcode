"""
22. Generate Parentheses
https://leetcode.com/problems/generate-parentheses/
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # DFS recursion
        # [1] Initialize result bojects, res = [] and
        # [2] define a helper function with input string and count of left parentheses
        # [3] Base case: if l == n and r == n, then append string to result
        # [4] Recursion: if l < n then recurse on s + '(' and if r < l recurse on s+')'
        # Complexity
        # If you know that there is a bijection of # of parentheses & catalan numbers and remember
        # Catalan numbers require O(4^n/n^.5) time complexity to generate and store.
        # Time: Calculate by Master Theorem T(n) = 2*T(n/2)
        # Otherwise
        # Time: Concatenating parenthesis is O(n) worst case and upper bound of # of parenthesis is 2^n
        # so O(n*2^n).
        # Space: O(n) for recursive call stack of at most size 2^(n-1) => O(n 2^n)
        def helper(n, l, r, s, i, res):
            if l == n and r == n:  # Base/terminal case
                res.append(s)
            if l < n: helper(n, l + 1, r, s+'(', i + 1, res)
            if l > r: helper(n, l, r + 1, s+')', i + 1, res)

        res = []
        helper(n, 0, 0, '', 0, res)
        return res

        # BFS
        # Complexity same as DFS

#         class ParenthesesString:
#             def __init__(self, str, l, r):
#                 self.str = str
#                 self.l = l
#                 self.r = r

#         from collections import deque
#         res = []
#         q = deque()
#         q.append(ParenthesesString("", 0, 0))
#         while q:
#             ps = q.popleft()
#             if ps.l == n and ps.r == n:
#                 res.append(ps.str)
#             if ps.l < n:
#                 q.append(ParenthesesString(ps.str + "(", ps.l + 1, ps.r))
#             if ps.l > ps.r:
#                 q.append(ParenthesesString(ps.str + ")", ps.l, ps.r + 1))
#         return res
