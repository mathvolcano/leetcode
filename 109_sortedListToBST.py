"""
109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # Recursion
        # [1] get the middle element of ll and make it the root
        # [2] split the ll to left & right parts
        # [3] Recurse to get to left and right parts of tree
        # [4] make left and right results the left & right tree nodes
        if not head: return None
        if not head.next: return TreeNode(val=head.val)

        # [2] make the middle element of list the root
        # [3] split the ll to left & right parts (cut left part's tail)
        def get_mid(head):
            # 2 pointers fast and slow
            slow = fast = head
            prev = None
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            prev.next = None  # Cut the left part from the middle
            return slow


        mid = get_mid(head)
        res = TreeNode(val=mid.val)
        res.left  = self.sortedListToBST(head)
        res.right = self.sortedListToBST(mid.next)
        return res
