"""
930. Binary Subarrays With Sum
https://leetcode.com/problems/binary-subarrays-with-sum/
"""

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        # [1] Use a prefix sum hash table
        # [2] Check if the complement is in the table and if so add that to count
        res = 0
        cur = 0  # current sum
        hash_table = {0: 1}
        for i, a in enumerate(A):
            cur += a
            res += hash_table.get(cur - S, 0)
            hash_table[cur] = hash_table.get(cur,0) + 1
        return res
