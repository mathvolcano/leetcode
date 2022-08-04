"""
1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
"""

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # Monotonic Queue with sliding window
        # [0.0] Initialize monotonic deques for tracking the max & min of a subarray
        # [0.1] Initialize a left pointer l = 0 and result object res = 0
        # for i,n in enumerate(nums):
        # [1.0] while max > max_d pop max_d. After loop add n
        # [1.1] while min > min_d pop min_d. After loop add n
        # [2] while the deque's max - min > limit check if head of queues equals nums[l]
        # if so popleft and increment l
        # [3] update result to be max(res & r-l+1). After loop return res
        # complexity: n = len(nums)
        # Time complexity O(n) with both pointers traversing nums at most once.
        # Space: O(n) worst case to store all elements in max_d & min_d with monotonic the worst case

        from collections import deque
        max_d, min_d = deque(), deque()
        l, res = 0, 0
        for r,n in enumerate(nums):
            while max_d and n > max_d[-1]:
                max_d.pop()
            max_d.append(n)
            while min_d and n < min_d[-1]:
                min_d.pop()
            min_d.append(n)

            while max_d[0] - min_d[0] > limit:
                if max_d[0] == nums[l]:
                    max_d.popleft()
                if min_d[0] == nums[l]:
                    min_d.popleft()
                l += 1
            res = max(res, r-l+1)
        return res
