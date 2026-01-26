class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def peek(self):
        return self.items[-1] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Stack after pushing:", stack.items)

print("Top item:", stack.peek())
print("Stack after peek:", stack.items)

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack.items)

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack.items)

print("Current size of stack:", stack.size())

popped_item = stack.pop()
print("Popped item:", popped_item)
print("Stack after popping:", stack.items)


print("Is the stack empty?", stack.is_empty())

print("size of stack", stack.size())