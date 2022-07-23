"""
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 2 pointers
        # [1] initialize l, r = 0, len(s) - 1
        # [2] if s[l] != s[r], check if s[l:r] is palindrome or s[l+1:r+1] is a palindrome and return
        # [3] must define a helper function to do that without storing extra copy of s
        # [4] else increment l & decrement r
        # Complexity: n = len(s)
        # Time: O(n) time
        # Space: O(1) for storing pointers

        def helper(s, p, q):
            while p < q:
                if s[p] != s[q]:
                    return False
                p += 1
                q -= 1
            return True

        l, r = 0, len(s) -1
        while l < r:
            if s[l] != s[r]:
                return helper(s, l+1, r) or helper(s,l, r-1)
            l += 1
            r -= 1
        return True

