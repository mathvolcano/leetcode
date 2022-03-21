"""
718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
"""

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        # Dynamic Programming
        # Let dp[i][j] denote the length of the longest prefix of nums1[i:] and nums2[j:]
        # O(n1 * n2) time and space
        n1, n2 = len(nums1), len(nums2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]
        for i in range(n1-1, -1, -1):
            for j in range(n2-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        return max(max(r) for r in dp)


        # Brute force
        # O(n1 * n2 * min(n1,n2)) time complexity for the 3 loops
        # O(1) space complexity
        # res = 0
        # for i in range(n1):
        #     for j in range(n2):
        #         k = 0
        #         while A[i+k] == B[j+k]:
        #             k += 1
        #         res = max(res, k)
        # return res
