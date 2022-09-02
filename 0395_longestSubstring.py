"""
395. Longest Substring with At Least K Repeating Characters
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Sliding window with hashmap
        # [1] Idea: find the max number of unique elements in s, denoted u, and perform a sliding
        # window over range(u) increasing window when < current unique & decreasing window
        # when more than unique. Updated hashmap count as needed.
        # [2] Update result when all values of hasmap are at least k.
        # Complexity: n = len(s) and u the number of unique chars in s (note this is at most 26)
        # Time: u iteration of outer loop, n iterations in inner loop, hashmap updates O(1) and all check is at most O(26) = O(1) so O(u)
        # Space O(1) space
        res = 0
        for c in range(1, len(set(s))+1):
            l, h = 0, {}
            for r, ch in enumerate(s):
                h[ch] = h.get(ch,0) + 1
                while len(h) > c:
                    cl = s[l]
                    h[cl] -= 1
                    if h[cl] == 0:
                        del h[cl]
                    l += 1
                if all(v >= k for v in h.values()):
                    res = max(res, r-l+1)
        return res
