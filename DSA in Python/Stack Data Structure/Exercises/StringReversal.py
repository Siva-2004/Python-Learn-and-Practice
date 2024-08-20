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

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def string_reverse(text):
    stack = Stack()
    for char in text:
        stack.push(char)
    for i in range(stack.size()):
        print(stack.pop(), end="")


if __name__ == "__main__":
    input_str = input("Enter the input string: ")
    string_reverse(input_str)
