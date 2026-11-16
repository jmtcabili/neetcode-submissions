class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMin = []

    def push(self, val: int) -> None:
        
        if (len(self.stack) == 0):
            self.stackMin.append(val)
        else:
            if (val <= self.stackMin[-1]):
                self.stackMin.append(val)
        self.stack.append(val)


    def pop(self) -> None:
        val = self.stack.pop()

        if (val == self.stackMin[-1]):
            self.stackMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMin[-1]
        
