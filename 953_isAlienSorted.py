"""
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/
"""

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        if n == 1: return True

        # Pythonic O(1) space, O(n*m) time
        # best case is O(n*m) because we may have to decode all letters in alls words

        # We can be more efficient by accessing each character only once.
        import string
        c_to_val = {x[0]: x[1] for x in zip(order, string.ascii_uppercase)}
        for i in range(1, n):
            encoded1 = ''.join([c_to_val[c] for c in words[i-1]])
            encoded2 = ''.join([c_to_val[c] for c in words[i]  ])
            if encoded1 > encoded2:
                return False
        return True
        