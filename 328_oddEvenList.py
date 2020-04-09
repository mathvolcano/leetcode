"""
328. Odd Even Linked List
https://leetcode.com/problems/odd-even-linked-list/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head

        odds_final = odds = ListNode(0)
        evens_final = evens = ListNode(0)
        parity = 0
        while head:
            parity = (parity + 1) % 2
            if parity == 1:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            if head.next:
                head = head.next
            else:
                break
        evens.next = None
        odds.next = evens_final.next
        return odds_final.next
