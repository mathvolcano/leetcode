"""
92. Reverse Linked List II
https://leetcode.com/problems/reverse-linked-list-ii/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # [1] Trivial case
        # [2] set c (current) = head and iterate down c until left is reached
        # [3] Set last previous part and last current parts to reconnect later
        # [4] Reverse sublist from left to right
        # [5] Reconnect lp with previous or else set head to previous and lc with current c
        # [6] return head
        # Complexity
        # n = len(head), then O(n) time and O(1) space

        if not head or left == right: return head

        c, p = head, None  # current, previous
        i = 1
        while i < left:
            p = c
            c = c.next
            i += 1

        lp, lc = p, c
        i = 0
        while i < right - left + 1:
            n = c.next
            c.next = p
            p = c
            c = n
            i += 1
        if lp:
            lp.next = p
        else:
            head = p
        lc.next = c
        return head
