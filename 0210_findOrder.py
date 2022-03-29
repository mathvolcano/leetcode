"""
210. Course Schedule II
https://leetcode.com/problems/course-schedule-ii/
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS with stack for topological sort

        # [1] Create a hashmap lookup of a course with its prereq & the prereq for the course
        # [2] Initialize a stack with courses that require no prereqs
        # [3] Iterate through the stack
        #  a. Pop the course in the stack and add to result and increment a counter
        #  b. Remove course from courses lookup that we need to examine
        #  c. Iterating through the prereq-to-course lookup add the courses to the stack associated with the course
        # [4] If the result has length equal to the number of courses then return the course list, else
        #     we have a cycle and return []
        # Time complexity: O(E+V) = O(numCourses + len(prerequisites))
        # Space complexity: O(E+V) = O(numCourses + len(prerequisites))
        from collections import defaultdict
        courses = defaultdict(set)
        pres = defaultdict(set)
        res = []

        for c, p in prerequisites:
            courses[c].add(p)
            pres[p].add(c)
        s = [n for n in range(numCourses) if not courses[n]]  # stack
        count = 0
        while s:
            no_pre = s.pop()
            res.append(no_pre)
            count+=1
            for c in pres[no_pre]:
                courses[c].remove(no_pre)
                if not courses[c]:
                    s.append(c)
        return res if count==numCourses else []
