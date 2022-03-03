"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # DFS – Encode as a graph a map of prerequisites to their dependent courses
        # Record status of the DFS (1 visited, 0 unvisited, -1 searching)
        # O(n^2)
        gr = [[] for x in range(numCourses)]
        for p in prerequisites:
            if p[0] not in gr[p[1]]:
                gr[p[1]].append(p[0])
        visit = [0 for _ in range(numCourses)]

        for c in range(numCourses):
            if visit[c] != 1:
                if not self.dfs(c, visit, gr):
                    return False
        return True


    def dfs(self, c, visit, gr):
        if visit[c] == 1:
            return True
        visit[c] = -1
        for i in gr[c]:
            if visit[i] == -1 or not self.dfs(i, visit, gr):
                return False
        visit[c] = 1
        return True
