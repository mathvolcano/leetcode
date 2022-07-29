"""
502. IPO
https://leetcode.com/problems/ipo/
"""
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Greedy Approach, 2 heaps
        # Find all projects that we can afford with our capital
        #.   & choose among them the project with the max profit.
        # [0] Add all project capitals to a min-heap
        # so that we can select a project with the smallest capital requirement.
        # [1] Go through the top projects of the min-heap
        # & filter the projects that can be completed within our available capital.
        # [2] Insert the profits of all these projects into a max-heap,
        # [3] Choose a project with the maximum profit.
        # [4] Repeat steps 1-3 for the number of projects.
        # Complexity:, p = len(profits) = len(capital)
        # Time: Worst case w > max(profits) & traverse entire lists each time
        # O(p lg p) for heapify + O(k* lg p) for k heappushes & pops
        # => O(max(k,p) lg p)
        # Space: O(p) additional space to store heaps
        from heapq import heappush, heappop
        c, p = [], [] # min capital heap, max profit heap
        for i,v in enumerate(capital):
            heappush(c, (v,i))

        while k > 0:
            while c and c[0][0] <= w:
                heappush(p, -profits[heappop(c)[1]])
            if not p:
                break
            w -= heappop(p)
            k -= 1
        return w
