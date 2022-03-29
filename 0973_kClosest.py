"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # Heap-based solution
        # [1] initialize a max heap, h, that tracks the points distance to origin
        # [2] Iterate through points:
        # a. add point & distance to heap if length of heap is < k
        # b. else, compute distance of point to origin and compare against max distance in heap
        # c. if new point has shorter distance then heappop heap and heappush new point
        # [3] return the resulting list of points in the heap
        # Time complexity: O(n log k) for heap
        # Space complexity: O(k)
        import heapq
        h = []
        for p in points:
            d = -(p[0]**2 + p[1]**2)
            if len(h) < k:
                heapq.heappush(h, (d, p[0], p[1]))
            elif (len(h) >= k) and (d > h[0][0]):
                # Python natively performs a min heap
                heapq.heappop(h)
                heapq.heappush(h, (d, p[0], p[1]))

        return [[x[1], x[2]] for x in h]


        # Pythonic Brute force
        # Time complexity: O(n log n) for n = len(points)
        # Space complexity: O(n) to compute distances
        # points.sort(key=lambda x: x[0]**2 + x[1]**2)
        # return points[:k]
