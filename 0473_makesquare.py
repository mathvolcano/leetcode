"""
473. Matchsticks to Square
https://leetcode.com/problems/matchsticks-to-square/
"""

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # DFS
        # [0] Create an array, square,  of length 4 that corresponds to
        # the length of each side.
        # [1] sort the array to speed up reaching the max side lengths
        # [2a] Termination condition: If the number of matchsticks
        # remaining is 0 and each side of square are equal then return True
        # [2b] If any side is bigger than the max theoretical side length then invalidate that square.
        # [3] Iterate via a DFS search by adding each matchstick to a square side
        # Time & space complexity: O(n log n + 4^n) = O(4^n) to iterate through all the combinations

        # Trivial Cases
        if len(matchsticks) < 4: return False
        sum_len = sum(matchsticks)
        if sum_len % 4 != 0: return False

        matchsticks.sort(key=lambda x: -x)

        square_len = sum_len // 4
        square = [0] * 4  # square
        return self.dfs(matchsticks, 0, square, square_len)


    def dfs(self, ms, idx, square, square_len):
        """matchsticks, idx, and square lengths, max square length."""
        if any(s > square_len for s in square):
            return False
        if idx >= len(ms):
            return all(s == square[0] for s in square)

        v = ms[idx]
        return (
                self.dfs(ms, idx + 1, [square[0]+v, square[1] ,square[2]  ,square[3]]  , square_len) or
                self.dfs(ms, idx + 1, [square[0]  ,square[1]+v,square[2]  ,square[3]]  , square_len) or
                self.dfs(ms, idx + 1, [square[0]  ,square[1]  ,square[2]+v,square[3]]  , square_len) or
                self.dfs(ms, idx + 1, [square[0]  ,square[1]  ,square[2]  ,square[3]+v], square_len)
        )
