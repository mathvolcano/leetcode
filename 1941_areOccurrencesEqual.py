"""
1941. Check if All Characters Have Equal Number of Occurrences
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
"""

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        # Let n = len(s). Time complexity: O(n) to traverse s.
        # Space at worse O(n) if string characters distinct
        from collections import Counter
        counts = Counter(s)
        prev = ''
        for c,v in counts.items():
            if not prev: prev = v
            if prev != v: return False
        return True
