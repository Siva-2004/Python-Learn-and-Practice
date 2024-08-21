from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.appendleft(value)

    def dequeue(self):
        if self.size() == 0:
            print("Empty queue")
            return
        return self.queue.pop()

    def front(self):
        return self.queue[-1]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)


if __name__ == "__main__":
    Q = Queue()
    Q.enqueue("1")

    for i in range(10):
        front = Q.front()
        print("   ", front)
        Q.enqueue(front + "0")
        Q.enqueue(front + "1")
        Q.dequeue()
