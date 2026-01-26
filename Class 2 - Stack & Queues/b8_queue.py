from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft() if self.items else None

    def peek(self):
        return self.items[0] if self.items else None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


queue = Queue()
print(queue.items)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue after enqueuing 1, 2, 3:")
print(queue.items)

print("Dequeue:", queue.dequeue())
print("Queue after dequeue:")
print(queue.items)

print("Peek:", queue.peek())
print("Is the queue empty?", queue.is_empty())


print("size of the queue:", queue.size())