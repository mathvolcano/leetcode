"""
621. Task Scheduler
https://leetcode.com/problems/task-scheduler/
"""

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter
        count = [value for value in Counter(tasks).values()]
        count.sort()
        max_freq = count.pop()
        diffs = max_freq-1
        idle = (diffs) * n
        while count and idle > 0:
            idle -= min(diffs, count.pop())
        return max(0, idle) + len(tasks)
