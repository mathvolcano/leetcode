"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
"""

def isAnagram(s, t):
    """O(nlogn) complexity based on sort."""
    return sorted(s) == sorted(t)

def isAnagram(s, t):
    """O(n) complexity based on sort – best case because we have to check all elements"""
    from collections import Counter
    return Counter(s) == Counter(t)