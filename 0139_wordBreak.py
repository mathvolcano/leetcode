"""
139. Word Break
https://leetcode.com/problems/word-break/
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP O(n*m) time, O(n) space
        n = len(s)
        if n == 0: return True
        if s in wordDict: return True

        valid = {0: True}
        for i in range(1, n+1):
            valid[i] = False
            for j in range(i):
                if valid[j] and (s[j:i] in wordDict):
                    valid[i] = True
                    break
        return valid[n]
