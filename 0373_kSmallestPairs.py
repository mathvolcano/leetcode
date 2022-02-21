"""
373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        # Heap
        # [0] Initialize a result list, res = []
        # [1] Create a min heap, h,  to store triplets (nums1[i] + nums2[j], nums[i], nums[j])
        # [2] Initialize a hashset, indices, of pairs of indices of nums1 and nums2 that have been added
        # and add (nums1[0], nums2[0]) to it.
        # [3] While k and h:
        #     [a] heappop h to add pair to res.
        #     [b] Add the next pairs of indices i+1, j and i, j+1 to the hashset
        #     [c] Add the triplets to the heap
        # Time complexity O(k log k) for k heappops of log k
        # Space complexity is O(k) to store all next pairs in the hashset and heap.
        from heapq import heappush, heappop
        res = []
        h = []  # min heap of triplets (nums1[i] + nums2[j], nums[i], nums[j])
        hs = set()  # set of indices (i, j) that have been indices to heap.
        def add(i, j):
            # Add (nums1[i] + nums2[j], i, j) to the heap if possible.
            if i < len(nums1) and j < len(nums2) and (i, j) not in hs:
                hs.add((i, j))
                heappush(h, (nums1[i] + nums2[j], i, j))

        add(0, 0)
        while k and h:
            k -= 1
            _, i, j = heappop(h)
            res.append((nums1[i], nums2[j]))
            add(i + 1, j)
            add(i, j + 1)
        return res


        # Brute Force with Heap
        # [1] Get all pairs of integers from nums1 and nums2 and their sum
        # [2] Form a min heap from the list based on the sums
        # [3] Return the first k pairs from the heap or the entiry list if k > the length of all pairs.
        # O(nm log nm) time complexity (to form product and sort)
        # O(nm) space complexity to store all pairs
        # from heapq import heapify, heappop
        # all_pairs_heap = [(n1+n2, n1, n2)
        #                   for n1 in nums1
        #                   for n2 in nums2]
        # heapify(all_pairs_heap)
        # if k < len(all_pairs_heap):
        #     return [heappop(all_pairs_heap)[1:] for _ in range(k)]
        # else:
        #     return [[x[1], x[2]] for x in all_pairs_heap]
