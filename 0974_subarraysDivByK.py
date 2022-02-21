"""
974. Subarray Sums Divisible by K
https://leetcode.com/problems/subarray-sums-divisible-by-k/
"""

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # [1] Use a hash_table to keep a running sum of A mod K, denoted s % K
        # [2] If the complement of s, s % K is in the hash_table then add its count to the
        # result. Update the count of s % K.
        # O(n) time and space.
        # Prefix sum solution - See 560. Subarray Sum Equals K
        res, s = 0, 0
        hash_map = {}
        hash_map[0] = 1   # Initialize so that elements divisible by K are added to res
        for a in A:
            s += a
            if s % K in hash_map:
                res += hash_map[s % K]
            hash_map[s % K] = hash_map.get(s % K, 0) + 1
        return res
