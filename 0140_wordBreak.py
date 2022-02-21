"""
140. Word Break II
https://leetcode.com/problems/word-break-ii/
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # DFS with Memoization
        # 1. Create a dict, memo, that maps to each index the set of all valid sentences up to index i in range(len(s))
        # 2. DFS – iterate through each index of range(len(s)) starting from len(s)-1 and going to 0.
        # 2a. If index i is done, return stored sentences, memo[i]
        # 2b. Iterate through indices in range(i, len(s)) and get the prefix from i to index s[i: j+1]
        # 2c. If the prefix is a word then get remaining valid sentences in s[j:] (obtained from dfs(j+1))
        # 2d. Append prefix to valid suffix results and add to result

        # Example: 'catsanddog'
        # {10: [''], 7: ['dog']}
        # No changes for indices 9,8
        # {10: [''], 7: ['dog'], 3: ['sand dog']}
        # No changes for indices 6,5,4
        # {10: [''], 7: ['dog'], 3: ['sand dog'], 4: ['and dog']}
        # No changes for indices 3,2,1
        # {10: [''], 7: ['dog'], 3: ['sand dog'], 4: ['and dog'], 0: ['cat sand dog', 'cats and dog']}
        # n = len(s), Time complexity O(n**2), Space complexity: O(2^n)

        # 2
        def dfs(i):
            if i in memo:
                return memo[i]
            res = []
            for j in range(i, len(s)):
                prefix = s[i: j+1]
                if prefix in wordDict:
                    tmp = dfs(j + 1)
                    for word in tmp:
                        res.append((prefix + " " + word).strip())
            memo[i] = res
            print(memo)
            return res


        wordDict = set(wordDict)
        memo = {len(s): [""]}  # 1
        return dfs(0)
