"""
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/
"""

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # Monotonic stack
        # Key idea: sum of subarray minimums that end at the i-th element in arr is
        # res[i] = res[j] + arr[i] * (i-j)
        # [0] Initialization
        #  a. add a leading zero to arr (to avoid accessing empty array)
        #. b. create a res list of the min subarray sums that end with index i
        #  c. initialize non-decreasing stack, s = [0], (leading zero to avoid accessing empty array)
        # [1] Iterate i,v through enumerate(arr)
        #. a. if arr[s[-1]] > v then pop stack
        #. b. get last remaining in stack
        #  c. set res[i] = res[j] + arr[i] * (i-j)
        #  d. append i to stack
        # [2] Return sum of result mod 10**9+7
        # O(n) time complexity & space complexity
        n = len(arr)
        arr = [0]+arr
        res = [0]*(n+1)
        s = [0]
        for i,v in enumerate(arr):
            while arr[s[-1]] > v:
                s.pop()
            j = s[-1]
            res[i] = res[j] + (i-j)*v
            s.append(i)
        MOD = 10**9+7
        return sum(res) % MOD

        # Brute Force
        # O(n^2) time & O(1) space
        # arr = [0] + arr
        # n = len(arr)
        # res = 0
        # for i in range(n):
        #     mn = arr[i]
        #     for j in range(i+1, n+1):
        #         res += min(arr[i:j])
        # return res
