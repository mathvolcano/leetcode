"""
716. Max Stack
https://leetcode.com/problems/max-stack/
"""

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_elems = []


    def push(self, x: int) -> None:
        self.stack += [x]
        if len(self.max_elems) == 0:
            self.max_elems += [x]
        else:
            self.max_elems += [max(self.max_elems[-1], x)]
        return


    def pop(self) -> int:
        if len(self.stack) > 0:
            self.max_elems.pop()
            return self.stack.pop()


    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]


    def peekMax(self) -> int:
        if len(self.max_elems) > 0:
            return self.max_elems[-1]


    def popMax(self) -> int:
        max_val = self.peekMax()

        # Iterate through the stack finding the top_most max eleemnt.
        buff = []
        while self.top() != max_val:
            buff.append(self.pop())
        self.pop()
        while len(buff) > 0:
            self.push(buff.pop())
        return max_val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()