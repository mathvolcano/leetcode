"""
657. Robot Return to Origin
https://leetcode.com/problems/robot-return-to-origin/
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # 2 counters
        # [1] initialize counters x = 0, y = 0 that track the x & y coordinates of the robot
        # [2] iterate through the string. If "U" then y += 1, if "D" then y -= 1
        #     if 'L' then x -= 1 and if 'R' then x += 1
        # [3] return True if x == y == 0 else False
        # O(len(s)) time and O(1) space

        x, y = 0, 0
        for m in moves:
            if m == 'L':
                x -= 1
            elif m == 'R':
                x += 1
            elif m == 'U':
                y += 1
            elif m == 'D':
                y -= 1
        return x == y == 0

        # Complex numbers – shorter & cleaner, but not as fast.
        # dic = {'L':-1, 'R':1, 'U':1j, 'D':-1j}
        # pos = 0
        # for m in moves:
        #     pos += dic[m]
        # return pos == 0
