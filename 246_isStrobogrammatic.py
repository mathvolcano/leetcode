"""
246. Strobogrammatic Number
https://leetcode.com/problems/strobogrammatic-number/
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dual = {'0': '0',
                '1': '1',
                '6': '9',
                '8': '8',
                '9': '6'}
        for i in range(len(num) // 2 + 1):
            if (num[-i - 1] not in dual) or (num[i] != dual[num[-i - 1]]):
                return False
        return True
