class MinStack:

    def __init__(self):
        # initialize a stack.
        self.stack=[]

    def push(self, val: int) -> None:
        # Each stack element is a tuple: (<element value>, <min value till that element>)
        minVal=self.stack[-1][1] if self.stack and val>self.stack[-1][1] else val
        self.stack.append((val, minVal))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]

# Time complexity: O(1) for all operations
# Space complexity: O(n)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()