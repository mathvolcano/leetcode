"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Fast & slow pointers
        # [1] get the length of the cycle by using a fast & slow pointer method
        # [2] initialize 2 pointers at head, p1 = p2 = head. Move p2 forward k spaces
        # [3] increment both pointers until p1 == p2 & return
        # O(n) time and O(1) space, where n = length(head)
        def length_of_cycle(head):
            f = s = head
            while f and f.next:
                f = f.next.next
                s = s.next
                if f == s:
                    return get_length(s)
            return 0

        def get_length(s):
            c = s  # current
            length = 0
            while True:
                c = c.next
                length += 1
                if c == s:
                    break
            return length

        p = head
        len_cycle = length_of_cycle(p)
        if len_cycle == 0: return None
        p1 = p2 = head
        while len_cycle:
            p2 = p2.next
            len_cycle -= 1
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
