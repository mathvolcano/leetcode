# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        # 0. Instantiate an empty TreeNode result to return for trivial case
        # 1. Get both the maximum value in nums and its index.
        # 2. Split nums into left and right subarrays relative to the max value's position in nums.
        # 3. Set result's root value to the max value.
        # 4. Recurse
        # 4a. Set l node to the result from applying to the l subarray
        # 4b. Set r node to the result from applying to the r subarray

        # Space complexity: O(n) for storing the tree
        # Time  complexity: T(n) = 2*T(n/2) + O(n) => O(n log n)


        if len(nums) == 0: return  # 0
        max_i, max_v = -float('inf'), -float('inf') # 1
        for i,v in enumerate(nums):
            if v > max_v:
                max_i, max_v = i, v
        return TreeNode(
            val = max_v,
            left = self.constructMaximumBinaryTree(nums[:max_i]),
            right = self.constructMaximumBinaryTree(nums[max_i+1:])
        )
