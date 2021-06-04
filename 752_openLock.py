"""
Open the Lock
https://leetcode.com/problems/open-the-lock/
"""

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # BFS
        # [1] Create a queue to store the (states, step) after n steps starting from ('0000',0)
        # [2a] Iterate through queue, popleft
        # [2b] if state is in target then return steps
        # [2c] else if not in deadends get neighbor states for the state
        # [3] Check if neighbor states are already visited (hash set), if not append to queue
        # [3] return -1 if queue empty

        # Let n be the number of digits of the lock
        # Space complexity is O(2^n) capped at total states so could be considered as O(1)
        # Time complexity: O(10^n) worst case because would have to check all digits.

        start = '0000'
        if start in deadends: return -1
        if start == target: return 0

        from collections import deque
        q = deque([(start, 0)])
        visited = set([start])
        while q:
            cur, steps = q.popleft()
            for i in range(4):
                for j in [-1, 1]:
                    nxt = cur[:i] + str((int(cur[i]) + j + 10) % 10) + cur[i+1:]
                    if nxt == target: return steps + 1
                    if nxt in deadends or nxt in visited: continue
                    q.append((nxt, steps + 1))
                    visited.add(nxt)
        return -1
