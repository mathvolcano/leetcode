"""
320. Generalized Abbreviation
https://leetcode.com/problems/generalized-abbreviation/
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        # DFS Backtrack
        # [0] Initialize a helper & a result list, res = [], and execute helper on it
        # [1] if pos = len(word) then append cur + str(count) to result if count > 0, else append cur
        # [2] else (continue), run helper on pos +1 and count +1
        # [3] and (abbreviate) run helper on pos +1 and add str(count) to current word
        # Complexity
        # Time: O(n * 2^n) for each character have at most 2 choices. Creating string takes n time
        # Space: O(n * 2^n) to store result each of length n. Excluding result, just O(n) to store string
        def helper(pos, cur, count):
            # pointer, current, count
            if len(word) == pos:
                # Once we reach the end, append current to the result
                res.append(cur + str(count) if count > 0 else cur)
            else:
                # Skip current position, and increment count
                helper(pos + 1, cur, count + 1)
                # Include current position, and zero-out count
                helper(pos + 1, cur + (str(count) if count > 0 else '') + word[pos], 0)

        res = []
        helper(0, '', 0)
        return res
