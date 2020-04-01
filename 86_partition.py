"""
86. Partition List
https://leetcode.com/problems/partition-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        s_iter = s_head = ListNode(0)
        l_iter = l_head = ListNode(0)

        while head:
            if head.val < x:
                s_iter.next = head
                s_iter = s_iter.next
            else:
                l_iter.next = head
                l_iter = l_iter.next
            head = head.next

        # Combine
        l_iter.next = None
        s_iter.next = l_head.next
        return s_head.next

