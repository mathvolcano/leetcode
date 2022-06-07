"""
2095. Delete the Middle Node of a Linked List
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [1] Use a fast & slow pointer to identify the middle node as the next node of slow
        # a. set s = head and f = head.next.next
        # b. while f & f.next, skip 2 nodes for f and skip 1 node for slow
        # [2] set the slow node's next to the next next
        # [3] return head
        # O(n) time and O(1) space

        if not head.next: return None
        s = head
        f = head.next.next
        while f and f.next:
            s = s.next
            f = f.next.next
        s.next = s.next.next
        return head


