"""
556. Next Greater Element III
https://leetcode.com/problems/next-greater-element-iii/
"""

class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Monotone Stack
        # Note we to replace the 1st descending digit from right to left to find a bigger number.
        # [0] initialize a result string res = -1 and cast n to a list of string digits
        # [1] Cast n to a string and iterate across the string from right to left
        #  a. We iterate the list from right to left and find the first digit that in descending order and this digit we called flag.
        # O(n) time complexity & space
        n = [x for x in str(n)]
        m = len(n)
        res = -1
        MOD = 2147483647
        for i in range(m-1, -1, -1):
            if n[i-1] < n[i] and i > 0:
                # If there is only one digit or if all dights on the right are same, then we will swap the flag and its first right digit.
                if i == m-1 or n[-1] == n[i]:
                    n[i-1], n[i] = n[i], n[i-1]
                    res = int(''.join(n))
                    return -1 if res > MOD else res
                else:
                    # Find the digit that greater than flag then swap those two and reverse the new right side
                    for j in range(m-1, i-1, -1):
                        if n[j] > n[i-1]:
                            n[i-1], n[j] = n[j], n[i-1]
                            break
                    res = int(''.join(n[:i] + n[i:][::-1]))
                return -1 if res > MOD else res
        return res
