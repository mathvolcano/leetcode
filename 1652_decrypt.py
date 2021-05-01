"""
1652. Defuse the Bomb
https://leetcode.com/problems/defuse-the-bomb/
"""

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        # [1] Idea: merge 2 copies of code into 1 array
        # [2]. Perform a sliding window size k for first n elements
        # O(n*k) time complexity, O(n) space

        n = len(code)
        if k == 0: return [0] * n
        code2 = code + code
        if k > 0:
            return [sum(code2[i+1: i+k+1]) for i in range(n)]
        if k < 0:
            return [sum(code2[n+i+k: n+i]) for i in range(n)]