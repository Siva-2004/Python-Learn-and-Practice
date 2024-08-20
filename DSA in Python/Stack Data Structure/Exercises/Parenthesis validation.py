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


def paranthesis_check(p1, p2):
    paranthesis_map = {"(": ")", "{": "}", "[": "]"}
    return paranthesis_map[p1] == p2


def validate_parenthesis(expr):
    stack = Stack()
    for ele in expr:
        if ele == "(" or ele == "[" or ele == "{":
            stack.push(ele)
        if ele == ")" or ele == "]" or ele == "}":
            if stack.size() == 0:
                return False
            if not paranthesis_check(stack.pop(), ele):
                return False
    return True


if __name__ == "__main__":
    input_str = input("Enter the input expression: ")
    print(validate_parenthesis(input_str))
