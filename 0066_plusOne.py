"""
66. Plus One
https://leetcode.com/problems/plus-one/
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # 1 Iterate through the digits array from right to left
        # 2 If digit is < 9 then add 1 to it & return
        # 3 Else, replace digit with 0 and continue to iterate until 2 is not satisfied
        # 4 If no digit is found then append 1 to the end of the array
        # O(n) time complexity, O(1) space complexity

        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1] + digits
