"""
784. Letter Case Permutation
https://leetcode.com/problems/letter-case-permutation/
"""

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # O(2^n) space complexity worst case because we have a bijection with binary strings and upper-lower cased words
        # O(n) time because we
        answer = ['']
        for s in S:
            if s.isalpha():
                answer = [a + c for a in answer for c in [s.lower(), s.upper()]]
            else:
                answer = [a + s for a in answer]
        return answer