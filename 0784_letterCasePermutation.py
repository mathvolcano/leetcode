"""
784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/
"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # Complexity: n = len(S)
        # Worst case when all characters are alphabet letters
        # Time: O(n*2^n) to generate all 2^n possibilities each one taking n time to iterate through s
        # sum_i i 2^i <= n sum_i 2^i = O(n * 2^n)
        # Space: O(n*2^n) complexity worst case because we have a bijection with
        # binary strings and upper-lower cased words and must traverse s (n) to construct answer
        # times traversing full bijection list of 2^n flipped

        res = ['']
        for s in S:
            if s.isalpha():
                res = [r + c for r in res for c in [s.lower(), s.upper()]]
            else:
                res = [r + s for r in res]
        return res