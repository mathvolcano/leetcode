"""
1381. Design a Stack With Increment Operation
https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""

class CustomStack:

    def __init__(self, maxSize: int):
        # Complexity O(n) space
        self.s = []
        self.n = maxSize
        self.i = []  # increment, i[k] element means all elements indices <= k must add self.i[k] to it

    def push(self, x: int) -> None:
        # O(1) time
        if len(self.i) < self.n:
            self.s.append(x)
            self.i.append(0)

    def pop(self) -> int:
        # O(1) pop
        if not self.i: return -1
        if len(self.i) > 1: self.i[-2] += self.i[-1]
        return self.s.pop() + self.i.pop()


    def increment(self, k: int, val: int) -> None:
        # O(1) time and space
        if self.i:
            self.i[min(k, len(self.i)) - 1] += val





# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)