"""
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""

def isPalindrome(s):
    # Trivial cases
    if len(s) <= 1: return True
    
    # Consider only alphanumeric & lower case
    simple_str_list = [c for c in s.lower() if c.isalnum()]
    simple_str = ''.join(simple_str_list)
    return simple_str == simple_str[::-1]


s = "A man, a plan, a canal: Panama"
isPalindrome(s)
#Output: true

s = "race a car"
isPalindrome(s)