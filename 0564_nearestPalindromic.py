"""
564. Find the Closest Palindrome
https://leetcode.com/problems/find-the-closest-palindrome/
"""
class Solution:
    def nearestPalindromic(self, s: str) -> str:

        # [Case 1]: If the final answer has the same number of digits as the input string S, then the answer must be the middle digits + (-1, 0, or 1) flipped into a palindrome.
        # Ex. 23456 had middle part 234, yielding candidates 233, 234, 235 flipped into a palindrome yields 23332, 23432, 23532
        # [Case 2] If the final answer has a different number of digits, it must be of the form 999....999 or 1000...0001, because any palindrome smaller than 99....99 or bigger than 100....001 will be farther away from s.
        # Time complexity: O(1) time because we always have at most 5 candidates
        # Space complexity O(1) space to store candidates

        l = len(s)
        # with different digits width, it must be either 10...01 or 9...9
        candidates = set((str(10 ** l + 1), str(10 ** (l - 1) - 1)))
        prefix = int(s[:(l+1)//2])
        for i in map(str, (prefix - 1, prefix, prefix + 1)):
            candidates.add(i + [i, i[:-1]][l & 1][::-1])
        candidates = set(candidates)
        candidates.discard(s)
        return min(candidates, key=lambda x: (abs(int(x) - int(s)), int(x)))


        # Brute Force - Really inefficient O(n) time complexity, O(1) space
        # Case1 : largest palindrome number < n
#         l = int(n) - 1
#         while not is_palindrome(str(abs(l))):
#             l -= 1

#         # Case2: smallest palindrome number > n
#         r = int(n) + 1
#         while not is_palindrome(str(r)):
#             r += 1

#         # Check absolute difference
#         if (abs(int(n) - l) > abs(int(n) - r)):
#             return str(r)
#         else:
#             return str(l)
