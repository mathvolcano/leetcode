"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
"""

def validPalindrome(s):
    def is_palindrome(s):
        return s == s[::-1]
    
    if len(s) <= 1:
        return True
    
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return is_palindrome(s[:l] + s[l+1:]) | is_palindrome(s[:r] + s[r+1:])
        l += 1
        r -= 1
    return True
