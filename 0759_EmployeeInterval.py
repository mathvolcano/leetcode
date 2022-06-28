"""
759. Employee Free Time
https://leetcode.com/problems/employee-free-time/
"""

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class EmployeeInterval:

    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval  # interval representing employee's working hours
        # index of the list containing working hours of this employee
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex  # index of the interval in the employee list

    def __lt__(self, other):
        # min heap based on meeting.end
        return self.interval.start < other.interval.start

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        # Use a heap and merge interval approach
        # [0] initialize a result tracker res = [] and a heap, h=[]
        # [1] Insert the first interval of each employee into a min heap
        # [2] while h
        # [3] if previousInterval is not overlapping with the next interval, append a free interval into result
        # [4] overlapping intervals, update the previousInterval if needed
        # [5] if there are more intervals available for the same employee, add their next interval
        # Complexity: n the total number of intervals and k the total number of employees
        # Time: O(n log k) for n heappushes/pops of O(lg k)
        # Space: O(k) because the heap will not have more than k entries
        from heapq import heappush, heappop
        if schedule is None: return []

        n = len(schedule)
        res, h = [], []
        for i in range(n):
            heappush(h, EmployeeInterval(schedule[i][0], i, 0))

        p = h[0].interval  # previous
        while h:
            q = heappop(h)  # queueTop
            if p.end < q.interval.start:  # no overlap
                res.append(Interval(p.end, q.interval.start))
                p = q.interval
            else:  # overlap, update previous interval if needed
                if p.end < q.interval.end:
                    p = q.interval
            es = schedule[q.employeeIndex]  # employeeSchedule
            if len(es) > q.intervalIndex + 1:
                heappush(h, EmployeeInterval(es[q.intervalIndex + 1], q.employeeIndex, q.intervalIndex + 1))
        return res