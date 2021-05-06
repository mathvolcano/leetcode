"""
1229. Meeting Scheduler
https://leetcode.com/problems/meeting-scheduler/
"""

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # [1]. Sort the arrays
        # [2]. Use 2 points on pointed at the start of slots1 and the other at slots2
        # [3]. Stop moving pointers once slots have overlapping range at least as long as duration.
        # [4]. Build the duration window as the min for th 2 pointers + the duration.
        # O(max(n1,n2) log max(n1,n2)) time complexity for sort, O(n) for space.

        slots1.sort()
        slots2.sort()

        p1 = 0
        p2 = 0
        n1, n2 = len(slots1), len(slots2)
        if n2 < n1:
            slots1, slots2 = slots2, slots1
            n1, n2 = n2, n1
        while p1 <= n1-1 and p2 <= n2-1:
            # start and ends
            s1, e1 = slots1[p1][0], slots1[p1][1]
            s2, e2 = slots2[p2][0], slots2[p2][1]

            latst_s = max(s1, s2)
            first_e = min(e1, e2)
            if first_e - latst_s >= duration:
                return [latst_s, latst_s + duration]
            else:
                if slots1[p1][1] == first_e: p1 += 1
                if slots2[p2][1] == first_e: p2 += 1
        return []
