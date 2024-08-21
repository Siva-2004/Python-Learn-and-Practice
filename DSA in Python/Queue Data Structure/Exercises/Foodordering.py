import threading
from collections import deque
import time


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


Q = Queue()


def Placeorder(orders: list):
    for order in orders:
        Q.enqueue(order)
        print("Order Placed: ", order)
        time.sleep(0.5)


def Serveorder():
    time.sleep(1)
    while not Q.is_empty():
        print("Order Served: ", Q.dequeue())
        time.sleep(2)


if __name__ == "__main__":
    orders = ["pizza", "samosa", "pasta", "biryani", "burger"]
    t1 = threading.Thread(target=Placeorder, args=(orders,))
    t2 = threading.Thread(target=Serveorder)
    t1.start()
    t2.start()
