"""
155. Min Stack
https://leetcode.com/problems/min-stack/
"""
class MinStack:

    def __init__(self):
        # 2 stack approach
        # [1] Create 1 stack to track the last values appended to the stack
        # [2] Create a 2nd stack to track the smallest elements of the stack
        #  a. (Improvement) to avoid adding duplicates we append the number of times the min
        #.    is appears in the stack so append to min stack (val, count)
        # O(n) space complexity & O(1) time for all operations
        self.s = [] # stack
        self.m = [] # min_stack

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.m or self.m[-1][0] >= val:
            self.m.append([val, 1])

    def pop(self) -> None:
        if self.s[-1] == self.m[-1][0]:
            if self.m[-1][1] > 1:
                self.m[-1][1] -= 1
            else:  # count == 1 so remove
                self.m.pop()
        self.s.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
