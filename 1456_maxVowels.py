"""
1456. Maximum Number of Vowels in a Substring of Given Length
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        # Sliding window
        # [1] maintain a window of size k with the cumulative number of vowels in it
        # e.g., 'eea' => [1,1, 1] and 'lee', => [0, 1,1]
        # [2] Updated sliding window by calculate the cumulative sum, s,  and update by subtracting k[0], pop k[0], then add 1 if vowel or 0 otherwise
        # time complexity: O(n), space complexity: O(k)
        from collections import deque
        w, sm, res = deque([0] * k), 0, 0  # window, sum, result
        for i, c in enumerate(s):
            sm -= w.popleft()
            val = 1 if c in 'aeiou' else 0
            sm += val
            if sm > res:
                res = sm
            if res == k: return k
            w.extend([val])
        return res
