from collections import deque

queue = deque()

# Add elements to the queue

queue.appendleft(14)
queue.appendleft(21)
queue.appendleft(25)

print(queue)

# Delete elements from the queue

print(queue.pop())
print(queue.pop())
print(queue.pop())

print(queue)
