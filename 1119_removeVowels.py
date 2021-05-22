"""
1119. Remove Vowels from a String
https://leetcode.com/problems/remove-vowels-from-a-string/
"""

class Solution:
    def removeVowels(self, s: str) -> str:
        # Pythonic - O(n) time and space
        return ''.join([c for c in s if c not in 'aeiou'])
