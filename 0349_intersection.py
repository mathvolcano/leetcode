"""
349. Intersection of Two Arrays
https://leetcode.com/problems/intersection-of-two-arrays/
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Use a hashtable Non-Pythonic O(n+m) time, O(1) space
        hash_table = {}
        for n in nums1:
            if n in hash_table:
                hash_table[n] = [hash_table[n][0]+1, 0]
            else:
                hash_table[n] = [1,0]
        for m in nums2:
            if m in hash_table:
                hash_table[m] = [hash_table[m][0], hash_table[m][1] + 1]
            else:
                hash_table[m] = [0, 1]
        return [x for x in hash_table if hash_table[x][0] and hash_table[x][1]]

        # Pythonic
        # return list(set(nums1).intersection(set(nums2)))
