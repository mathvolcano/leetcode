"""
1721. Swapping Nodes in a Linked List
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        if not head: return head

        # Get ll values into an array
        node_vals = []
        while head:
            node_vals.append(head.val)
            head = head.next

        # Swap kth value & Reconstruct ll from array
        node_vals[k-1], node_vals[-k] = node_vals[-k], node_vals[k-1]
        root = tail = ListNode(-1)
        while node_vals:
            tail.val = node_vals.pop(0)
            if node_vals:
                tail.next = ListNode(-1)
            tail = tail.next
        return root
