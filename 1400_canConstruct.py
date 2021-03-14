"""
1400. Construct K Palindrome Strings
https://leetcode.com/problems/construct-k-palindrome-strings/
"""

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Trivial cases
        if not s or (len(s) < k): return False

        # Get counts of characters
        from collections import Counter
        char_counts = Counter(s)
        n_odd_counts = len([c for c in char_counts if char_counts[c] % 2 == 1])
        # By the Pigeonhole Principle if the number of characters with odd counts exceeds k
        # then we will always have at least one of these characters not fit into the k substrings because
        # these characters must be a middle char in the substrings.
        return n_odd_counts <= k