from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        return self.queue.pop()

    def peek(self):
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    Q = Queue()

    # Inserting elements in to the queue
    Q.enqueue(14)
    Q.enqueue(21)
    Q.enqueue(25)
    print(Q.queue)

    print(Q.peek())
    print(Q.queue)

    # Deleting elements from the queue
    print(Q.dequeue())
    print(Q.dequeue())

    print(Q.queue)
