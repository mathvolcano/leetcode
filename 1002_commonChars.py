"""
1002. Find Common Characters
https://leetcode.com/problems/find-common-characters/
"""

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # O(n*m) time with n number of words and m average word length
        # O(m) space for the hashes
        if len(A) == 1: return list(A[0])

        from collections import Counter
        counts = Counter(A[0])
        for word in A:
            counts &= Counter(word)

        res = []
        for l, count in counts.items():
            res += [l] * count
        return res
