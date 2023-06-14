class MinStack:

    def __init__(self):
        self.minStack = []
        self.ourList = []
    def push(self, val: int) -> None:
        # if(list[-1]< val):
        #     temp = self.ourList.pop()
        #     self.ourList.append(val)
        #     self.ourList.append(temp)
        # dare I mess with the insertion??
        # yes yes lmfaoo but a different stack

        self.ourList.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.ourList.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.ourList[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()