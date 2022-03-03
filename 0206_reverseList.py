"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # Both ways are O(n) time and O(n) space

        ### Recursive Solution
        if not head or (not head.next): return head

        # Recurse
        start = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return start

        ### Iterative Solution
        # Get reversed values
        n = head
        new_list = []
        while n:
            new_list.insert(0, n.val)
            n = n.next

        # Change values in place
        r = head
        for v in new_list:
            r.val = v
            r = r.next
        return head