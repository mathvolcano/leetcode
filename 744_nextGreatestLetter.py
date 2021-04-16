"""
744. Find Smallest Letter Greater Than Target
https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        # Trivial cases
        if len(letters) == 2:
            return letters[0] if letters[0] > target else letters[1]

        # Deal with wrap now
        # so we can assume that there is an element after target in letters
        if (letters[-1] <= target) or (letters[0] > target): return letters[0]

        # Binary search
        l, r = 0, len(letters) - 1
        while l < r:
            m = (l + r) // 2
            if target < letters[m]:
                r = m
            else:
                l = m + 1
        return letters[l]
