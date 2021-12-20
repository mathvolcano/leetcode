"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Pythonic brute force: O(n log n) time, O(1) additional space
        # if len(nums) == 0: return 0
        # nums.sort(reverse=True)
        # return nums[k-1]

        # (Min) Heap: O(n log k) time complexity, O(k) additional space
        from heapq import heappush, heappop
        h, res = [], -float('inf')
        for n in nums:
            if len(h) < k:
                heappush(h, n)
            elif n > res:
                heappush(h, n)
                heappop(h)
            res = min(h)
        return res

        # Faster in Leetcode, but have to run more heappushes & slower in theory.
        # from heapq import heappush, heappop
        # heap = []
        # for num in nums:
        #     heappush(heap,-num)
        # for i in range(k):
        #     res = heappop(heap)
        # return -res
