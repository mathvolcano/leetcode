"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head: return head

        n = 0
        dummy1 = dummy2 = head
        while dummy1:
            n += 1
            dummy1 = dummy1.next

        from math import floor
        mid = floor(n / 2)

        while mid:
            dummy2 = dummy2.next
            mid -= 1
        return dummy2
