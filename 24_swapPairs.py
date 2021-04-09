# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next): return head

        # 1. Swap the first two nodes in the list, i.e. head and head.next;
        # 2. Recurse call swap(head.next.next)
        # 3. Attach the returned head of the sub-list in step (2)

        tail = None
        if head.next.next:
            tail = head.next.next

        if head.next:
            temp = head
            head = head.next
            head.next = temp
            head.next.next = tail

        if tail:
            swapped_ll = self.swapPairs(tail)
            head.next.next = swapped_ll
        return head




        