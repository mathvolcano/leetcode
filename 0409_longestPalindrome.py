"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        # Note that the longest palindrome is the number of even characters
        # + 1 for any single character that has an odd occurence
        # O(n) time complexity for count and summing the result
        # O(1) additional space complexity for the hash map.
        res = 0
        has_odd = 0
        for l, c in counts.items():  # letter, count
            res += (c // 2) * 2  # Remove odd counts
            if c % 2 == 1:
                has_odd = 1
        return res + has_odd
