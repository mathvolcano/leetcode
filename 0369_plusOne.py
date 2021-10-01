"""
369. Plus One Linked List
https://leetcode.com/problems/plus-one-linked-list/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        # 2 pointer Approach

        # last_non9: tracks the position of the last digit < 9
        # p = travels the ll
        # Add 1 to last_non9, set the remaining nodes in the tail to 0.

        # Steps
        # 1 Initialize a results list, res with next the head
        # 2 Initialize pointer nodes to track position, p, and last_non9 node
        # 3 Iterate through p and update last_non9
        # 4 Add 1 to last_non9
        # 5 Iterate through tail of last_non9 and set values to 0
        # 6 Return res ll.
        # O(n) time complexity and O(1) space

        res = ListNode(0)
        res.next = head
        last_non9 = res
        p = res

        while p.next:
            p = p.next
            if p.val < 9:
                last_non9 = p

        last_non9.val += 1
        while last_non9.next:
            last_non9 = last_non9.next
            last_non9.val = 0

        return res if res.val > 0 else res.next
