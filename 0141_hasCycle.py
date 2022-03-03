"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def hasCycle(head):
    visited = set()

    while head:
        if head not in visited:
            visited.add(head)
        else:
            return True
        head = head.next
    return False
