"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # Fast & Slow pointer
        # [1] initialize a fast pointer, f = head and keep head as a slow pointer
        # [2] while f and f.next then increment head once and f twice
        # [3] return head
        # O(len(head)) time and O(1) space, but 1 pass
        f = head
        while f and f.next:
            head = head.next
            f = f.next.next
        return head

        # [1] Get the length, l, of the ll by iterating a copy of head
        # [2] Get middle count, m = l // 2
        # [3] increment head by m
        # O(len(head)) time and O(1) space, but 1.5 iterations of head
        # ll = head
        # l = 0
        # while ll:
        #   l += 1
        #   ll = ll.next
        # m = l // 2
        # while m:
        #   head = head.next
        #   m -= 1
        # return head
