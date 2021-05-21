"""
1704. Determine if String Halves Are Alike
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # [1] split the string in half
        # [2] add 1 for each char in the halves if the char is a vowel
        # [3] compare counts

        vowels = 'aeiouAEIOU'
        mid = len(s) // 2
        sum1 = sum(1 for x in s[:mid] if x in vowels)
        sum2 = sum(1 for x in s[mid:] if x in vowels)
        return sum1 == sum2
