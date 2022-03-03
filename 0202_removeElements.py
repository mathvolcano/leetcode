"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head: return head
        tmp = ListNode(0)
        result = tmp

        while head:
            if head.val != val:
                tmp.next = head
                tmp = tmp.next
            else:
                tmp.next = None
            head = head.next

        return result.next
