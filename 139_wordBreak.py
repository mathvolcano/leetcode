"""
139. Word Break
https://leetcode.com/problems/word-break/
"""

def wordBreak(s, wordDict):
    """DP: O(n*m)."""
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

s = "leetcode"
wordDict = ["leet", "code"]
wordBreak(s, wordDict)

s = "applepenapple"
wordDict = ["apple", "pen"]
wordBreak(s, wordDict)

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
wordBreak(s, wordDict)
