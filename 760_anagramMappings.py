"""
760. Find Anagram Mappings
https://leetcode.com/problems/find-anagram-mappings/
"""

class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # hash Map - O(n) time and space
        # [1] Create a hashmap so that
        # [2] return the lookup [hm[x] for x in nums1]
        hm = {nums2[i]: i for i in range(len(nums1))}
        return [hm[x] for x in nums1]
