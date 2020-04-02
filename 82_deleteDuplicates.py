"""
82. Remove Duplicates from Sorted List II
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next): return head

        result = ListNode(0)
        result.next = head
        no_dups = result
        ahead = result.next

        # Check if the next value is distinct and iterate
        while no_dups.next:
            # Advance ahead to last dup
            while ahead.next and (no_dups.next.val == ahead.next.val):
                ahead = ahead.next

            # If different nodes then advance
            if no_dups.next == ahead:
                ahead = ahead.next
                no_dups = no_dups.next
            else:  # step to same next node
                no_dups.next = ahead.next

        return result.next
