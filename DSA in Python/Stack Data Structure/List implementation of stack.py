"""
Stack can be implemented using the list in python. The methods that are used are:
1. append - to add an element to the stack.
2. pop - to remove the element from the top of the stack.

The major disadvantage is the complexity that we will encouter due to resizing of the list.
The entire list must be copied and pasted in new location where extra memeory is located.

"""

stack = []

# Insert elements to the stack

stack.append(4)
stack.append(2)
stack.append(21)

# delete elements from the stack

print(stack.pop())
print(stack.pop())
print(stack.pop())
