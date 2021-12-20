"""
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


def findKthLargest(nums, k):
    if len(nums) == 0:
        return 0
    
    nums.sort(reverse=True)
    return nums[k-1]

ex1 = [3,2,1,5,6,4]
k1 = 2
assert findKthLargest(ex1, k1) == 5

ex2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
assert findKthLargest(ex2, k2) == 4

ex1 = [3,2,1,5,6,4]
k1 = 2
assert findKthLargest(ex1, k1) == 5