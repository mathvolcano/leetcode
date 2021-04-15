"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # In each iteration, search an insert operations of hash map
        # take O(1)/O(logn) time in average/worst cases.
        # Thus, time complexity will be O(n)/O(nlogn) in average/worst cases.

        # Hash map O(1) space, O(n) time for 1 pass of nums
        hash_map = {}
        # Only store largest value because we march forward in nums
        for j, n in enumerate(nums):
            if (n in hash_map) and abs(j - hash_map[n]) <= k: return True
            hash_map[n] = j
        return False