"""
1152. Analyze User Website Visit Pattern
https://leetcode.com/problems/analyze-user-website-visit-pattern/
"""

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        from collections import defaultdict
        from itertools import combinations
        import heapq

        # Time complexity is O(n log n) for sort where n = len(usernames)
        triples = list(zip(timestamp,username,website))
        triples = sorted(triples)  # Can improve this step by sorting for each users sites only

        # [2] Get user histories
        uh = defaultdict(list)
        for _, u, w in triples:
            uh[u].append(w)

        # get various combinations possible for various users
        pattern_counts = defaultdict(int)
        for _, w in uh.items():
            u_patterns = set(combinations(w,3))  # O(min(w^3, w^(w-k))) time complexity
            for up in u_patterns:
                pattern_counts[up] -= 1

        # Return most common element using a heap, can instead just get most common in O(1) time.
        c = list(zip(pattern_counts.values(), pattern_counts.keys()))
        heapq.heapify(c)  # O(1)
        return heapq.heappop(c)[1]
