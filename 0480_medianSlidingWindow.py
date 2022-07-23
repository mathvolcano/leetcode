"""
480. Sliding Window Median
https://leetcode.com/problems/sliding-window-median/
"""

import heapq
from heapq import heapify, heappop, heappush
class Solution:

    def __init__(self):
        self.l = []  # max heap
        self.h = []  # min heap

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Sliding window & median
        # [1] Create 2 heaps to track median with the lower half of elements a max heap and
        # an array of higher elements a min heap
        # [2] Use a sliding window of size k to insert k elements into heaps in a balanced way.
        # Ie, at each iteration, we insert a new number in the heaps, we need to remove one number
        # from the heaps which is going out of the sliding window.
        # [3] After the removal, we need to rebalance the heaps in the same way that we did while inserting.
        # Complexity: n = len(nums)
        # Time
        # calculating each median is O(k)
        # Finding and removing and index is O(k + lg k)
        # n -k +1 iterations => Time O(nk)
        # Space
        # O(n-k+1) for storing result
        # O(k) for storing median heaps
        # Total = O(n)
        res = [0.0 for x in range(len(nums) - k + 1)]
        for i, v in enumerate(nums):
            # Populate heaps
            if not self.l or v <= -self.l[0]:
                heappush(self.l, -v)
            else:
                heappush(self.h, v)
            self.rebalance_heaps()

            j = i - k + 1
            if j >= 0:  # if we have at least 'k' elements in the sliding window
                # add the median to the the result array
                if len(self.l) == len(self.h):
                    res[j] = -self.l[0] / 2.0 + self.h[0] / 2.0
                else:
                    res[j] = -self.l[0] / 1.0

                # remove the element going out of the sliding window
                d = nums[i - k + 1]  # to delete
                if d <= -self.l[0]:
                    self.remove(self.l, -d)
                else:
                    self.remove(self.h, d)

                self.rebalance_heaps()
        return res


    def remove(self, h, e):  # heap, element
        # removes an element from the heap keeping the heap property
        i = h.index(e)  # find the element
        # move the element to the end and delete it
        h[i] = h[-1]
        del h[-1]
        # we can use heapify to readjust the elements but that would be O(N),
        # instead, we will adjust only one element which will O(logN)
        if i < len(h):
            heapq._siftup(h, i)
            heapq._siftdown(h, 0, i)

    def rebalance_heaps(self):
        # either both the heaps will have equal number of elements or max-heap will have
        # one more element than the min-heap
        ll, lh = len(self.l), len(self.h)
        if ll > lh + 1:
            heappush(self.h, -heappop(self.l))
        elif ll < lh:
            heappush(self.l, -heappop(self.h))
