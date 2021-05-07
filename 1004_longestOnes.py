"""
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/
"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        # [1] Create a queue to track last indices of flips
        # [2] Iterate through the nums and increment the left side of the window when
        # we encounter a flip.
        # [3] Update the longest run and increment right side of window.
        # O(n) time to iterate through nums, O(k) space to track k indices.

        flips = [-1] if k > 0 else []  # queue of last indices where a flip was needed
        res = 0  # trivial queue of last indices, result
        l = 0  # left side of window
        for r in range(len(nums)):
            if nums[r] == 0:
                if len(flips) < k:
                    flips.append(r)
                else:
                    # Assign left
                    if k == 0:
                        l = r + 1
                    else:
                        l = flips.pop(0) + 1
                        flips.append(r)
            res = max(res, r - l + 1)

        return res
