"""
587. Erect the Fence
https://leetcode.com/problems/erect-the-fence/
"""

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        """Monotone Chain Convex Hull https://algorithmist.com/wiki/Monotone_chain_convex_hull.
        O(nlog(n))"""
        def orientation(p, q, r):
            """Compare slopes. 0 - Colinear points, 1 - clockwise, 2 - counterclockwise"""
            val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1]))
            if (val > 0):
                return 1
            elif (val < 0):
                return 2
            else:
                return 0

        # Degenerate
        if len(points) <= 2:
            return points

        points.sort()


        upper = []
        for p in points:
            # Remove the last point if it's above the upper hull
            while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) == 1:
                upper.pop()
            upper.append(p)

        lower = []
        for p in reversed(points):
            # Remove the last point if it's below the lower hull
            while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) == 1:
                lower.pop()
            lower.append(p)

        # Remove last point because
        return list(map(list, set(map(tuple, lower[:-1] + upper[:-1]))))