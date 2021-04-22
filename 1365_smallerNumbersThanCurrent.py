"""
1365. How Many Numbers Are Smaller Than the Current Number
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Brute force is O(n^2)
        # Sort is O(nlog n) time complexity, hash is O(1) and nums copy is O(n) space
        if len(nums) == 1: return [0]

        from collections import defaultdict
        nums2 = nums.copy()
        nums2.sort()
        val_to_count = defaultdict(int)
        for i, v in enumerate(nums2):
            val_to_count[v] += 0 if v == nums2[i - 1] else i
        return [val_to_count[v] for v in nums]
