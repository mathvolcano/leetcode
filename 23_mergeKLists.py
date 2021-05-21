# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # Recursion
        # [1] Create 2 linked lists: heads = tail
        # [2] Define merge helper that modifies tail in place
        # [2a] Base/terminating case: if not l1/l2 append l2/l1 to tail. Return
        # [2b] if l1/l2 is smaller than l2/l1 then append node to tail and set l1/l2 to next.
        # [3] Recurse and merge again if [2] holds
        # [4] Time: O(n + m) complexity and O(n+m) space complexity for new head & tail

        def merge(node, l1, l2):
            if not l1:
                node.next = l2
                return
            if not l2:
                node.next = l1
                return

            if l1.val < l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node = node.next
            merge(node, l1, l2)

        head = tail = ListNode(0)
        merge(tail, l1, l2)
        return head.next


        # Iterative procedure (merge sort)
        # [1] Create 2 linked lists: heads = tail 
        # [2] until we end l1 or l2 if l1's head is smaller than l2's then append to tail's next
        # else append l2's head to tail's next
        # [3] update tail's head to next
        # [4] append the remainder of l1 or l2 to tail
        # [4] return head
        # Time & Space complexity: O(n + m)
#         if not l1: return l2
#         if not l2: return l1

#         head = tail = ListNode(0)

#         while l1 and l2:
#             if l1.val < l2.val:
#                 tail.next , l1 = l1, l1.next
#             else:
#                 tail.next, l2 = l2, l2.next
#             tail = tail.next
#         tail.next = l1 or l2

#         return head.next