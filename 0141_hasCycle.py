"""
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Fast & slow pointer method
        # [1] initialize fast & slow pointers at head f = s = head
        # [2] while f and f.next are not none increment f twice and s once.
        # [3] check if f == s and if so break
        # O(n) time and O(1) space, where n = length of head
        f = s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False


        # Hash set
        # n = len(head) then O(n) time and space
#         visited = set()

#         while head:
#             if head not in visited:
#                 visited.add(head)
#             else:
#                 return True
#             head = head.next
#         return False

