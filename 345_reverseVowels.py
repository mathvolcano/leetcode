"""
345. Reverse Vowels of a String
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        # 2-pointer solution
        # [1] Set left l and right r pointers to word endpoints
        # [2] increment l & r until they reach voewl or l > r
        # swap s[l] and s[r]
        # O(n) time and O(n) space to create array

        n = len(s)
        vowels = 'aeiouAEIOU'
        l, r = 0, n - 1
        arr = list(s)  # str types are not mutable
        while l < r:
            while l < n and s[l] not in vowels:
                l += 1
            while r > 0 and s[r] not in vowels:
                r -= 1
            if l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l + 1, r - 1
        return ''.join(arr)
