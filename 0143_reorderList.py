"""
143. Reorder List
https://leetcode.com/problems/reorder-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # [1] Use fast/slow pointers to find the mid of the list and split ll into 2 halves
        # [2] reverse order of 2nd list half
        # [3] Intertwine the 2 list halves
        # [4] return head of new list
        # O(n) time and O(1) space
        s = f = head
        while f and f.next:
            s = s.next
            f = f.next.next

        def reverse(h):
            p = None  # previous
            while h:
                n = h.next # next
                h.next = p
                p = h
                h = n
            return p
        h2 = reverse(s)

        h1 = head
        while h1 and h2:
            n1 = h1.next
            h1.next = h2
            h1 = n1

            n2 = h2.next
            h2.next = h1
            h2 = n2

        if h1:
            h1.next = None
