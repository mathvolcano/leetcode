"""
148. Sort List
https://leetcode.com/problems/sort-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head: return head

        # Get values & sort
        vals = []
        temp = head
        while temp:
            vals.append(temp.val)
            temp = temp.next
        vals.sort()

        # Construct new list
        new_head = head
        result = ListNode(0)
        result.next = new_head
        while new_head:
            new_head.val = vals.pop(0)
            new_head = new_head.next

        return result.next