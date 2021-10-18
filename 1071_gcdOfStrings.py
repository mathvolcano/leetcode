"""
1071. Greatest Common Divisor of Strings
https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        # Recursion
        # [0] Base case - if str1 is empty return str2 & vice versa
        # [1] if len(str2) > len(str1), then swap str1 & str2 and recurse
        # [2] If start of str1 == str2 then Recurse on str1[len(str2):], str2
        # [3] Else, return ''

        # Example 1:
        # gcd(str1 = "ABCABC", str2 = "ABC")
        # Pass 1: str1[:len(str2)] == 'ABC' == str2
        # Pass 2: gcd('ABC', '') => 'ABC'

        # Example 2:
        # gcd(str1 = "ABABAB", str2 = "ABAB")
        # Pass 1: str1[:len(str2)] == 'ABAB' == str2
        # Pass 2: gcd('AB', 'ABAB') => gcd('ABAB', 'AB')
        # Pass 3: gcd('AB', 'AB') => 'AB'

        # Example 4:
        # gcd(str1 = "ABCDEF", str2 = "ABC")
        # Pass 1: str1[:len(str2)] == 'ABC' == str2
        # Pass 2: gcd('DEF', 'ABC') => ''

        # Complexity
        # s1 = len(str1), s2 = len(str2). Assume s2 < s1.
        # Then O(s1+s2) time complexity to check substring match. O(s1) space for storing substring.

        if not str1 or not str2:
            return str1 if str1 else str2
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
