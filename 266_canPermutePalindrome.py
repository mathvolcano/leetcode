"""
266. Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/
"""

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # [1] Count the number of letters in s
        # [2] If the counts has more than letter that is odd then return False
        from collections import Counter
        counts = Counter(s)
        res = 0
        for l,c in counts.items():
            if c % 2 == 1:
                res += 1
            if res > 1:
                return False
        return True
