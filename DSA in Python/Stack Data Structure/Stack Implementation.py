from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def print(self):
        print(self.stack)


if __name__ == "__main__":
    stack = Stack()
    stack.push(13)
    stack.push(14)
    print(stack.size())
    stack.print()
    print(stack.peek())
    stack.print()
    print(stack.pop())
    stack.print()
    print(stack.pop())
    print(stack.is_empty())
