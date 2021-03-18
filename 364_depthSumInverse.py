"""
364. Nested List Weight Sum II
https://leetcode.com/problems/nested-list-weight-sum-ii/
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger], depth=1) -> int:
        """O(n) because we have to check every array element."""
        if not nestedList: return 0

        depth_totals = []
        depth = 0
        while nestedList:
            depth_totals.append(0)
            newNestedList = []
            for x in nestedList:
                if x.isInteger():
                    depth_totals[depth] += x.getInteger()
                else:
                    for y in x.getList():
                        newNestedList.append(y)

            nestedList = newNestedList
            depth += 1
        return sum([v*(len(depth_totals)-i) for i, v in enumerate(depth_totals)])
