"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Hash set O(n)
        hash_set = set()
        for n in nums:
            if n in hash_set:
                return True
            else:
                hash_set.add(n)
        return False

        # Pythonic - O(n)
        # return True if len(set(nums)) < len(nums) else False
