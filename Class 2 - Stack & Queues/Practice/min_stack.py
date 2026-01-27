class MinStack:

    def __init__(self):
        self.items = [] #in this stack we will store pairs (value, currMin)

    def push(self, val: int) -> None:
        if (len(self.items) == 0):
            self.items.append([val, val])
        else:
            currMin = self.items[-1][1]
            if val < currMin:
                currMin = val
            self.items.append([val, currMin])

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]
    

obj = MinStack()
obj.push(5)
obj.push(-2)
obj.push(100)
obj.push(-1)
obj.pop()
print(obj.top())
print(obj.getMin())
