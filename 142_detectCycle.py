"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:

        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

            if slow is fast:
                node = head
                while node is not slow:
                    node = node.next
                    slow = slow.next
                return node
        return None

