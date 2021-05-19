"""
719. Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance/
"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        # Binary Search
        # [1] sort nums
        # [2] The range of all distances we must search is [0, nums[-1] - nums[0]].
        # We perform a binary search on this range
        # [3] Given x (starting at midpoint) count the number of pairs whose MAB
        # is bigger than m.
        nums.sort()  # [1]

        def helper(m):  # [3]
            count = l = 0
            for i in range(len(nums)):
                while nums[i] - nums[l] > m:
                    l += 1
                count += i - l
            return count >= k

        # [2] Binary Search
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if helper(m):
                r = m
            else:
                l = m + 1
        return l

        # Brute force Use a max heap to store the k smallest elements
        # [1] compute all pairs
        # [2] for a given pair compute distance
        # [3] if distance is smaller than max of the heap then push pop
        # O(n log k) time and O(k) space
#         from heapq import heapify, heappushpop

#         h = []  # heap

#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1, n):
#                 # print('i, j', i,j)
#                 diff = abs(nums[i] - nums[j])
#                 if len(h) < k:
#                     heappush(h, -diff)
#                 else:
#                     if -diff > h[0]:
#                         heappushpop(h, -diff)
#                 # print('h', h)
#         return -h[0]