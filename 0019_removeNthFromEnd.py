"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head

    first = second = dummy
    for _ in range(n):
        first = first.next

    while first.next:
        first, second = first.next, second.next
    else:
        second.next = second.next.next

    return dummy.next
